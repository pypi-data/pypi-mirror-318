"""
This module holds the AESModeCTR wrapper class using tgcrypto.
"""
import tgcrypto


class AESModeCTR:
    """Wrapper around tgcrypto's AES CTR mode with custom IV"""

    def __init__(self, key: bytes, iv: bytes):
        """
        Initializes the AES CTR mode with the given key/iv pair.

        :param key: the key to be used as bytes. Must be 16, 24, or 32 bytes long.
        :param iv: the bytes initialization vector. Must have a length of 16.
        """
        assert isinstance(key, bytes)
        assert len(key) in (16, 24, 32)  # AES key lengths
        assert isinstance(iv, bytes)
        assert len(iv) == 16

        self._key = key
        self._iv = iv

    def encrypt(self, data: bytes):
        """
        Encrypts the given plain text through AES CTR.

        :param data: the plain text to be encrypted.
        :return: the encrypted cipher text.
        """
        cipher = tgcrypto.AESModeCTR(self._key, self._iv)
        return cipher.encrypt(data)

    def decrypt(self, data: bytes):
        """
        Decrypts the given cipher text through AES CTR.

        :param data: the cipher text to be decrypted.
        :return: the decrypted plain text.
        """
        cipher = tgcrypto.AESModeCTR(self._key, self._iv)
        return cipher.decrypt(data)