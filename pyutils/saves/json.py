from .base import DataLoader
from json import dumps, loads
from ..structure.dict import update


class JsonDataLoader(DataLoader):
    def encode(self, data):
        return dumps(data, **self.options)

    def decode(self, raw):
        return loads(raw)

    def get_default_file_extension(self):
        return 'json'