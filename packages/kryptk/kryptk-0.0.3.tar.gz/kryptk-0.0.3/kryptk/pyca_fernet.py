# coding: utf-8

from cryptography.fernet import Fernet
import hashlib
import base64
import random
from ksupk import utf8_to_bytes, bytes_to_utf8

from kryptk.interfaces import IKey, ICipher
from kryptk.utils import EncodedEntity

class PycaFernetKey(IKey):
    """
    Key class for PycaFernet
    """

    def __init__(self, x: str | bytes | EncodedEntity | None):
        if x is None:
            self.key =base64.urlsafe_b64encode(hashlib.sha256(random.randbytes(random.randint(10**3, 10**7))).digest())
        elif isinstance(x, str):
            self.key = base64.urlsafe_b64encode(hashlib.sha256(x.encode("utf-8")).digest())
        elif isinstance(x, bytes):
            self.key = base64.urlsafe_b64encode(hashlib.sha256(x).digest())
        elif isinstance(x, EncodedEntity):
            self.key = x.get_as_bytes()
        else:
            raise ValueError(f"x (\"{x}\") must be str or bytes. ")

    def get_as_bytes(self) -> bytes:
        return self.key

    def dump(self) -> EncodedEntity:
        return EncodedEntity(self.key)


class PycaFernet(ICipher):
    """
    PyCA Fernet wrapper. See https://cryptography.io/en/latest/fernet
    (https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py)
    """

    def __init__(self, key: PycaFernetKey | None):
        if key is None:
            key = PycaFernetKey(None)
        elif not isinstance(key, PycaFernetKey):
            raise ValueError("(PycaFernet.__init__) key must be PycaFernetKey")
        self.key = key
        self.__f = Fernet(self.key.get_as_bytes())

    def encrypt(self, x: str | bytes) -> str | bytes:
        try:
            if isinstance(x, str):
                str_bytes = False
                data = utf8_to_bytes(x)
            elif isinstance(x, bytes):
                str_bytes = True
                data = x
            else:
                raise ValueError("Encrypt only str or bytes. ")
        except Exception as e:
            raise ValueError("(encrypt) Wrong params. ")

        try:
            en = self.__f.encrypt(data)
        except Exception as e:
            raise RuntimeError("Problem with encryption. ")

        if str_bytes:
            return en
        else:
            return base64.b64encode(en).decode("ascii")

    def decrypt(self, x: str | bytes) -> str | bytes:
        try:
            if isinstance(x, str):
                str_bytes = False
                data = base64.b64decode(x.encode("ascii"))
            elif isinstance(x, bytes):
                str_bytes = True
                data = x
            else:
                raise ValueError("Encrypt only str or bytes. ")
        except Exception as e:
            raise ValueError("(decrypt) Wrong params. ")

        try:
            de = self.__f.decrypt(data)
        except Exception as e:
            raise RuntimeError("Problem with decryption. ")

        if str_bytes:
            return de
        else:
            return bytes_to_utf8(de)

    def get_key(self) -> IKey:
        return self.key
