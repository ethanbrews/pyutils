from .base import DataLoader
from ..file import readfile, writefile
import plistlib


class PListLoader(DataLoader):
    def get_default_file_extension(self):
        return 'plist'

    def save(self, data):
        writefile(self.fname, plistlib.dumps(data), 'wb+')

    def load(self):
        try:
            with open(self.fname, 'rb') as f:
                return plistlib.load(f)
        except FileNotFoundError:
            return self.default