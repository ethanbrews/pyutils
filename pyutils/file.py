import os
from .errors import OutOfOptionsError
from .structure.list import flatten as flatten_list
from random import SystemRandom
import shutil


def readfile(f, mode='r'):
    """Reads the entirety of a file and returns it"""
    with open(f, mode) as fobj:
        return fobj.read()


def writefile(f, s, mode='w+'):
    """Writes all of the input to the file"""
    with open(f, mode) as fobj:
        return fobj.write(s)


def readfilelines(f, mode='r'):
    """Reads the file one line at a time"""
    with open(f, mode) as fobj:
        for line in fobj:
            yield line


class FilenameGenerators:
    @staticmethod
    def numerical_generator(start=1):
        def wrap():
            nonlocal start
            while True:
                yield start
                start += 1

    @staticmethod
    def random_generator(length=16, alphabet=None):
        if alphabet is None:
            alphabet = flatten_list([[chr(x) for x in range(97, 123)], [chr(x).upper() for x in range(97, 123)], [str(x) for x in range(10)], ['_']])
        def wrap():
            random = SystemRandom()
            while True:
                yield ''.join(random.choice(alphabet) for _ in range(length))

        return wrap


def ensuredir(d):
    os.makedirs(d, exist_ok=True)


def dir_empty(d):
    try:
        return len(os.listdir(d)) == 0
    except FileNotFoundError:
        return True


def is_empty(df):
    if os.path.isdir(df):
        return dir_empty(df)
    elif os.path.isfile(df):
        return file_empty(df)


def file_empty(f):
    try:
        return os.path.getsize(f) == 0
    except FileNotFoundError:
        return True


def clear_directory(directory):
    for root, dirs, files in os.walk(directory):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


def get_next_filename(d, base, gen=FilenameGenerators.numerical_generator()):
    for item in gen():
        fname = os.path.join(d, base % item)
        if not os.path.exists(fname):
            return fname

    raise OutOfOptionsError('The generator exited before an available file name was found')

