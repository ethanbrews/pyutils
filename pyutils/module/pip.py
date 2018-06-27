import subprocess
import tempfile
import os.path
from ..file import get_next_filename, FilenameGenerators, ensuredir
from ..environment import get_executable
from site import addsitedir

def EXECUTE(command):
    sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sp.wait()
    return sp.returncode == 0

INSTALL_ROOT = os.path.join(tempfile.gettempdir(), get_next_filename(tempfile.gettempdir(), '%s', FilenameGenerators.random_generator()))
GET_DIRECTORY = lambda directory, module: os.path.join(directory, get_next_filename(directory, '%s.%%s' % module, FilenameGenerators.random_generator()))


def install_module(module, directory=INSTALL_ROOT, get_directory=GET_DIRECTORY):
    directory = get_directory(directory, module)
    ensuredir(directory)
    cmd = ' '.join([get_executable(), '-m', 'pip', 'install', '--target="%s"' % directory, module])
    success = EXECUTE(cmd)
    if not success:
        raise RuntimeError('Command failed to execute "%s"' % cmd)
    addsitedir(directory)