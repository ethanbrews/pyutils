from .base import DataLoader
from ..structure.dict import flatten, update


class ProperyLoader(DataLoader):
    def __init__(self, *args, delimiter='.', **kwargs):
        super().__init__(*args, **kwargs)
        self.delimiter = delimiter

    def get_default_file_extension(self):
        return 'properties'

    def encode(self, data):
        data = flatten(data, self.delimiter)
        return '\n'.join(['{}={}'.format(k, data[k]) for k in data])

    def decode(self, raw):
        lst = [(p[0], p[1]) for p in [line.split('=') for line in raw.split('\n') if (line != '' and (not line.startswith('#')))]]
        d = {}
        for item in lst:
            _u = {}
            u = _u
            keys = item[0].split(self.delimiter)[:-1]
            for k in keys[:-1]:
                u[k] = {}
                u = u[k]
            u[item[0][-1]] = item[1]
            update(d, _u)
        return d

