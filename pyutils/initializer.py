from functools import wraps
from .structure.dict import merge as merge_dict
import inspect


def initializer(fun):
    names, varargs, keywords, defaults = inspect.getargspec(fun)

    @wraps(fun)
    def wrapper(self, *args, **kargs):
        for name, arg in merge_dict(dict(zip(names[1:], args)), kargs).items():
            setattr(self, name, arg)
        fun(self, *args, **kargs)

    return wrapper
