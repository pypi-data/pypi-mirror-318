# coding: utf-8

from abc import ABC, abstractmethod
from kryptk.utils import EncodedEntity


class IKey(ABC):
    """
    Key interface for objects that implemented ICipher
    """

    @abstractmethod
    def __init__(self, x: str | bytes | EncodedEntity | None):
        pass

    def dump(self) -> EncodedEntity:
        pass


class ICipher(ABC):
    """
    Interface for ciphers.
    """

    @abstractmethod
    def __init__(self, key: IKey | None):
        """
        Init cipher with its class key.
        if key == None, then create IKey randomly
        :param key: cipher key
        """
        pass

    @abstractmethod
    def encrypt(self, x: str | bytes) -> str | bytes:
        """
        Encrypting.
        If x is str, then str will be returned, which must be putted inside decrypt.
        If x is bytes, then bytes will be returned, which must be putted inside decrypt.
        :param x: text or bytes to encrypt.
        :return: encrypted text or bytes
        """
        pass

    @abstractmethod
    def decrypt(self, x: str | bytes) -> str | bytes:
        """
        Decrypt text or bytes encrypted by encrypt.
        If x is a str, it returns the same text as it was passed to the encrypt function.
        if x is a bytes, it returns the same bytes as it was passed to the encrypt function.

        ``` python
        text = f"utf-8 text needed to encrypt. "  # The same behavior applies to bytes.
        key_text = f"Secret utf-8 key"  # The same behavior applies to bytes.
        key = IKey(key_text)  # Key object with interface ICipher
        cipher = ICipher()  # Some object with interface ICipher
        assert text == cipher.decrypt(cipher.encrypt(text))
        ```

        :param x:
        :return: decrypted text or bytes
        """
        pass

    @abstractmethod
    def get_key(self) -> IKey:
        """
        Get cipher key from this cipher.
        :return: cipher key
        """
        pass
