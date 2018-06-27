from pyutils import file
from pyutils import initializer
from pyutils import structure
from pyutils import module


def start(name): print('START %s' % name.upper())

def end(name): print('END %s\n' % name.upper())

start('FILE IO')
file.writefile('test.txt', 'Test String')
print(file.readfile('test.txt'))
end('FILE IO')


start('INITIALIZER')


class TestClass:
    @initializer
    def __init__(self, var=0, **kwargs):
        pass

test_class = TestClass(5, var2='hello, world!')
print(test_class.var)
print(test_class.var2)

end('INITIALIZER')


start('DICTS')

print('Merge {{\'a\':\'b\'}} & {{\'c\': \'d\'}}: {}'.format(structure.dict.merge({'a': 'b'}, {'c': 'd'})))
print("Flatten {{'a': 'b', 'c': {{'d': 'e'}}}}: {}".format(structure.dict.flatten({'a': 'b', 'c': {'d': 'e'}})))
print("Update {{'a': {{'b': 'c', 'd': 'e'}}}} with {{'a': {{'b': 'f'}}}}: {}".format(structure.dict.update({'a': {'b': 'c', 'd': 'e'}}, {'a': {'b': 'f'}})))

end('DICTS')

start('STRUCT')

d = {'a': 'b', 'c': 'd'}
sd = structure.Struct(**d)
print('{} -> {}'.format(d, sd))

end('STRUCT')

start('LISTS')

print('Flatten [1, [2, [3]], 4, [5, 6, [[7]]]]: ', structure.list.flatten([1, [2, [3]], 4, [5, 6, [[7]]]]))

end('LISTS')

start('MODULE INSTALLER')

module.pip.install_module('Pillow')
import PIL

end('MODULE INSTALLER')
