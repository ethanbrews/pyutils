import json
from base64 import b64encode, b64decode


class JSONLoader:
    @staticmethod
    def _save(d):
        return json.dumps(d)

    @staticmethod
    def _load(j):
        return json.loads(j)

    @classmethod
    def load(cls, path, default):
        try:
            with open(path) as f:
                return cls._load(f.read())
        except FileNotFoundError:
            return default

    @classmethod
    def save(cls, path, d):
        f = open(path, "w+")
        f.write(cls._save(d))
        f.close()

    @staticmethod
    def load_and_fill_missing(path, default, *args):
        for d in args:
            default.update(d)
        default.update(JSONLoader.load(path, default))
        return default


class CompressedDataLoader(JSONLoader):
    @staticmethod
    def _save(d):
        return b64encode(JSONLoader._save(d).encode()).decode()

    @staticmethod
    def _load(j):
        return JSONLoader._load(b64decode(j.encode()).decode())


class ListLoader:
    def __init__(self, delimeter='\uE000'):  # First Unicode PUA char
        self.delimeter = delimeter

    def _save(self, l):
        return self.delimeter.join(l)

    def _load(self, s):
        return [i for i in s.split(self.delimeter) if i != '']

    def load(self, path, default=None):
        if default is None:
            default = []

        try:
            with open(path) as f:
                return self._load(f.read())
        except:
            return default

    def save(self, path, l, mode='w+'):
        with open(path, mode) as f:
            f.write(self._save(l))


class CompressedListLoader(ListLoader):
    def _load(self, s):
        return super()._load(b64decode(s))

    def _save(self, l):
        return b64encode(super()._save(l))