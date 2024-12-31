from os.path import getsize as os_size, join as os_join
import asyncio
from hashlib import md5
from typing import Optional
from inspect import isawaitable
from math import ceil
from typing import (
    AsyncGenerator,
    BinaryIO,
    DefaultDict,
    Optional,
    Tuple,
    Union,
    Callable
)
from time import time as get_time
from datetime import datetime

from .. import utils, helpers
from ..network import MTProtoSender
from .telegramclient import TelegramClient
from ..tl.alltlobjects import LAYER
from ..tl.functions import InvokeWithLayerRequest
from ..tl.functions.auth import (
    ExportAuthorizationRequest,
    ImportAuthorizationRequest,
)
from ..tl.functions.upload import (
    GetFileRequest,
    SaveBigFilePartRequest,
    SaveFilePartRequest,
)
from ..tl.types import (
    Document,
    InputDocumentFileLocation,
    InputFile,
    InputFileBig,
    TypeInputFile,
    InputMediaUploadedDocument
)

######################################################################################

filename: str = ''

TypeLocation = Union[Document, InputDocumentFileLocation]

class DownloadSender:
    """Handles downloading files from Telegram."""
    
    def __init__(self, client: TelegramClient, sender: MTProtoSender, file: TypeLocation, offset: int, limit: int, stride: int, count: int) -> None:
        self.client = client
        self.sender = sender
        self.request = GetFileRequest(file, offset=offset, limit=limit)
        self.stride = stride
        self.remaining = count

    async def next(self) -> Optional[bytes]:
        """Fetch the next chunk of data."""
        if not self.remaining:
            return None
        result = await self.client._call(self.sender, self.request)
        self.remaining -= 1
        self.request.offset += self.stride
        return result.bytes

    async def disconnect(self) -> None:
        """Disconnect the sender."""
        await self.sender.disconnect()

class UploadSender:
    """Handles uploading files to Telegram."""
    
    def __init__(self, client: TelegramClient, sender: MTProtoSender, file_id: int, part_count: int, big: bool, index: int, stride: int) -> None:
        self.client = client
        self.sender = sender
        self.part_count = part_count
        self.request = SaveBigFilePartRequest(file_id, index, part_count, b"") if big else SaveFilePartRequest(file_id, index, b"")
        self.stride = stride
        self.previous = None

    async def next(self, data: bytes) -> None:
        """Upload the next part of the file."""
        if self.previous:
            await self.previous
        self.previous: Optional[asyncio.Task] = asyncio.create_task(self._next(data))

    async def _next(self, data: bytes) -> None:
        """Internal method to upload a part of the file."""
        self.request.bytes = data
        await self.client._call(self.sender, self.request)
        self.request.file_part += self.stride

    async def disconnect(self) -> None:
        """Disconnect the sender."""
        if self.previous:
            await self.previous
        await self.sender.disconnect()

class ParallelTransferrer:
    """Manages parallel file transfers to and from Telegram."""
    
    def __init__(self, client: TelegramClient, dc_id: Optional[int] = None) -> None:
        self.client = client
        self.loop = self.client.loop
        self.dc_id = dc_id or self.client.session.dc_id
        self.auth_key = self.client.session.auth_key if not (dc_id and self.client.session.dc_id != dc_id) else None
        self.senders = None
        self.upload_ticker = 0

    async def _cleanup(self) -> None:
        """Clean up the senders after transfer completion."""
        await asyncio.gather(*[sender.disconnect() for sender in self.senders])
        self.senders = None

    @staticmethod
    def _get_connection_count(file_size: int, max_count: int = 30, full_size: int = 64 * 1024 * 1024) -> int:
        """Calculate the number of connections needed based on file size."""
        return max_count if file_size > full_size else ceil((file_size / full_size) * max_count)

    async def _init_download(self, connections: int, file: TypeLocation, part_count: int, part_size: int) -> None:
        """Initialize download senders."""
        minimum, remainder = divmod(part_count, connections)

        def get_part_count() -> int:
            nonlocal remainder
            if remainder > 0:
                remainder -= 1
                return minimum + 1
            return minimum

        self.senders = [
            await self._create_download_sender(file, 0, part_size, connections * part_size, get_part_count()),
            *await asyncio.gather(
                *[self._create_download_sender(file, i, part_size, connections * part_size, get_part_count()) for i in range(1, connections)]
            ),
        ]

    async def _create_download_sender(self, file: TypeLocation, index: int, part_size: int, stride: int, part_count: int) -> DownloadSender:
        """Create a download sender."""
        return DownloadSender(self.client, await self._create_sender(), file, index * part_size, part_size, stride, part_count)

    async def _init_upload(self, connections: int, file_id: int, part_count: int, big: bool) -> None:
        """Initialize upload senders."""
        self.senders = [
            await self._create_upload_sender(file_id, part_count, big, 0, connections),
            *await asyncio.gather(
                *[self._create_upload_sender(file_id, part_count, big, i, connections) for i in range(1, connections)]
            ),
        ]

    async def _create_upload_sender(self, file_id: int, part_count: int, big: bool, index: int, stride: int) -> UploadSender:
        """Create an upload sender."""
        return UploadSender(self.client, await self._create_sender(), file_id, part_count, big, index, stride)

    async def _create_sender(self) -> MTProtoSender:
        """Create a new MTProto sender."""
        dc = await self.client._get_dc(self.dc_id)
        sender = MTProtoSender(self.auth_key, loggers=self.client._log)
        await sender.connect(self.client._connection(dc.ip_address, dc.port, dc.id, loggers=self.client._log, proxy=self.client._proxy))
        
        if not self.auth_key:
            auth = await self.client(ExportAuthorizationRequest(self.dc_id))
            self.client._init_request.query = ImportAuthorizationRequest(id=auth.id, bytes=auth.bytes)
            req = InvokeWithLayerRequest(LAYER, self.client._init_request)
            await sender.send(req)
            self.auth_key = sender.auth_key
            
        return sender

    async def init_upload(self, file_id: int, file_size: int, part_size_kb: Optional[float] = None, connection_count: Optional[int] = None) -> Tuple[int, int, bool]:
        """Initialize the upload process."""
        connection_count = connection_count or self._get_connection_count(file_size)
        part_size: int = (part_size_kb or utils.get_appropriated_part_size(file_size)) * 1024
        part_count: int = (file_size + part_size - 1) // part_size
        is_large = file_size > 10 * 1024 * 1024
        await self._init_upload(connection_count, file_id, part_count, is_large)
        return part_size, part_count, is_large

    async def upload(self, part: bytes) -> None:
        """Upload a part of the file."""
        await self.senders[self.upload_ticker].next(part)
        self.upload_ticker = (self.upload_ticker + 1) % len(self.senders)

    async def finish_upload(self) -> None:
        """Finish the upload process."""
        await self._cleanup()

    async def download(self, file: TypeLocation, file_size: int, part_size_kb: Optional[float] = None, connection_count: Optional[int] = None) -> AsyncGenerator[bytes, None]:
        """Download a file from Telegram."""
        connection_count= connection_count or self._get_connection_count(file_size)
        part_size: int = (part_size_kb or utils.get_appropriated_part_size(file_size)) * 1024
        part_count: int = ceil(file_size / part_size)
        await self._init_download(connection_count, file, part_count, part_size)

        part = 0
        while part < part_count:
            tasks = [self.loop.create_task(sender.next()) for sender in self.senders]
            for task in tasks:
                data = await task
                if not data:
                    break
                yield data
                part += 1
        await self._cleanup()

parallel_transfer_locks: DefaultDict[int, asyncio.Lock] = DefaultDict(lambda: asyncio.Lock())

def stream_file(file_to_stream: BinaryIO, chunk_size=1024):
    """Stream a file in chunks."""
    while True:
        data_read = file_to_stream.read(chunk_size)
        if not data_read:
            break
        yield data_read

async def _internal_transfer_to_telegram(client: TelegramClient, response: BinaryIO, progress_callback: Callable) -> Tuple[TypeInputFile, int]:
    """Transfer a file to Telegram."""
    file_id = helpers.generate_random_long()
    file_size = os_size(response.name)

    hash_md5 = md5()
    uploader = ParallelTransferrer(client)
    part_size, part_count, is_large = await uploader.init_upload(file_id, file_size)
    buffer = bytearray()
    
    for data in stream_file(response):
        if progress_callback:
            r = progress_callback(response.tell(), file_size)
            if isawaitable(r):
                try:
                    await r
                except Exception:
                    pass
        if not is_large:
            hash_md5.update(data)
        if len(buffer) == 0 and len(data) == part_size:
            await uploader.upload(data)
            continue
        new_len = len(buffer) + len(data)
        if new_len >= part_size:
            cutoff = part_size - len(buffer)
            buffer.extend(data[:cutoff])
            await uploader.upload(bytes(buffer))
            buffer.clear()
            buffer.extend(data[cutoff:])
        else:
            buffer.extend(data)
    
    if len(buffer) > 0:
        await uploader.upload(bytes(buffer))
    await uploader.finish_upload()
    
    if is_large:
        return InputFileBig(file_id, part_count, filename), file_size
    else:
        return InputFile(file_id, part_count, filename, hash_md5.hexdigest()), file_size

async def download_file(client: TelegramClient, location: TypeLocation, out: BinaryIO, size: int, progress_callback: Optional[Callable] = None) -> BinaryIO:
    """Download a file from Telegram."""
    dc_id, location = utils.get_input_location(location)
    downloader = ParallelTransferrer(client, dc_id)
    downloaded = downloader.download(location, size)
    
    async for x in downloaded:
        out.write(x)
        if progress_callback:
            r = progress_callback(out.tell(), size)
            if isawaitable(r):
                try:
                    await r
                except Exception:
                    pass

    return out

async def upload_file(client: TelegramClient, file: BinaryIO, name: str, progress_callback: Optional[Callable] = None) -> TypeInputFile:
    """Upload a file to Telegram."""
    global filename
    filename = name
    return (await _internal_transfer_to_telegram(client, file, progress_callback))[0]

async def media_download(client, message, path):
    try:
        mime_type = ''
        attributes = ''
        current_time = str(int(get_time()))
        if message.photo:
            try:
                size = message.media.photo.sizes[-1].sizes[-1]
            except:
                try:
                    size = message.media.photo.sizes[-1].size
                except:
                    pass
            dt = datetime.fromisoformat(str(message.media.photo.date))
            file_name = 'Photo_' + str(dt.strftime("%Y-%m-%d-%H-%M-%S")) + ' ' + current_time + '.png'
        else:
            mime_type = message.media.document.mime_type
            _temp = mime_type.split('/')
            file_ext = _temp[1]
            attributes = message.media.document.attributes
            if message.file.name:
                file_name = message.file.name
                size = message.file.size
            else:
                dt = datetime.fromisoformat(str(message.media.document.date))
                file_name = file_ext + '_' + str(dt.strftime("%Y-%m-%d-%H-%M-%S")) + ' ' + current_time + '.' + file_ext
                size = message.media.document.size
        file_path = os_join(path, file_name)
        with open(file_path, "wb") as download_handler:
            await download_file(client, message.media, download_handler, size)
            return file_name, mime_type, attributes
    except:
        return False

async def media_upload(client, entity, file_name, path, photo: bool, caption, mime_type, attributes):
    try:
        file_path = os_join(path, file_name)
        with open(file_path, "rb") as in_data:
            res = await upload_file(client, in_data, file_name)
            if photo:
                await client.send_message(entity, caption, file=res)
            else:
                media = InputMediaUploadedDocument(
                    file=res,
                    mime_type=mime_type,
                    attributes=attributes,
                    force_file=False
                )
                await client.send_message(entity, caption, file=media)
    except:
        return False

######################################################################################