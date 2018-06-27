class Struct:
    def __init__(self, **entries):
        def conv(v):
            if isinstance(v, dict):
                return Struct(**v)
            return v

        entries = {k: conv(entries[k]) for k in entries}
        self.__dict__.update(entries)
        self._names = [k for k in entries]

    def __str__(self):
        d = self.to_dict()
        return 'Struct{%s}' % ", ".join(['%s: %s' % (k, d[k]) for k in d])

    def to_dict(self):
        def conv(val):
            if isinstance(val, Struct):
                return val.to_dict()
            return val

        return {k: conv(self.__dict__[k]) for k in self._names}