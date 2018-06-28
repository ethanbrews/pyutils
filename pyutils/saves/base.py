from .. import file
from ..structure.dict import update

class DataLoader:
    def __init__(self, filename, default=None, **options):

        self.fname = filename if '.' in filename else '%s.%s' % (filename, self.get_default_file_extension())
        self.default = {} if default is None else default
        self.options = options

    def load(self):
        try:
            return update(self.default, self.decode(file.readfile(self.fname)))
        except FileNotFoundError:
            return self.default

    def save(self, data):
        file.writefile(self.fname, self.encode(data))

    def encode(self, data):
        raise NotImplementedError()

    def decode(self, raw):
        raise NotImplementedError()

    def get_default_file_extension(self):
        return 'txt'
