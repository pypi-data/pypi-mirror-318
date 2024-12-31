"""
AES IGE implementation in Python.

If available, cryptg will be used instead, otherwise
if available, libssl will be used instead, otherwise
the Python implementation will be used.
"""
import tgcrypto
import logging


__log__ = logging.getLogger(__name__)

class AES:
    """
    Class that servers as an interface to encrypt and decrypt
    text through the AES IGE mode.
    """
    @staticmethod
    def decrypt_ige(cipher_text: bytes, key: bytes, iv: bytes) -> bytes:
        """
        Decrypts the given text in 16-bytes blocks by using the
        given key and 32-bytes initialization vector.
        """
        return tgcrypto.ige256_decrypt(cipher_text, key, iv)

    @staticmethod
    def encrypt_ige(plain_text: bytes, key: bytes, iv: bytes) -> bytes:
        """
        Encrypts the given text in 16-bytes blocks by using the
        given key and 32-bytes initialization vector.
        """
        plain_text += bytes(-len(plain_text) % 16)
        
        return tgcrypto.ige256_encrypt(plain_text, key, iv)