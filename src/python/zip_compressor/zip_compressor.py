import zlib


class ZipCompressor:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def compress(text: str):
        return zlib.compress(text.encode('utf-8'))

    @staticmethod
    def decompress(text: str):
        return zlib.decompress(text).decode('utf8')
