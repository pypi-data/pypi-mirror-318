# coding: utf-8

import base64


class EncodedEntity:
    def __init__(self, x: bytes | str):
        if isinstance(x, str):
            self.x = base64.urlsafe_b64decode(x.encode("utf-8"))
        elif isinstance(x, bytes):
            self.x = x
        else:
            raise ValueError(f"EncodedEntity (\"{x}\") must be str or bytes. ")

    def get_as_str(self) -> str:
        return base64.urlsafe_b64encode(self.x).decode("utf-8")

    def get_as_bytes(self) -> bytes:
        return self.x
