import collections


def merge(x, y):
    """Merge x with z, overwriting x with z where applicable"""
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


def update(d, u):
    """
    :param d: Dictionary of items which will be overwritten
    :param u: Dictionary of items which will overwrite values in d
    :returns: D updated to contain values in u
    """
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


def flatten(d, delimiter='.'):
    def expand(key, value):
        if isinstance(value, dict):
            return [ (key + delimiter + k, v) for k, v in flatten(value).items() ]
        else:
            return [ (key, value) ]

    items = [ item for k, v in d.items() for item in expand(k, v) ]

    return dict(items)