import sys
import os
from warnings import warn


def get_executable():
    ex = sys.executable
    parts = ex.split(os.sep)
    parts[-1] = parts[-1].replace('pythonw', 'python')
    exn = os.sep.join(parts)
    if os.path.exists(exn):
        return exn
    warn('Python executable may not be valid. The expected executable name did not exist.')
    return ex