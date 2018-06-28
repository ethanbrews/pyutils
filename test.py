from pyutils import file
from pyutils import initializer
from pyutils import structure
from pyutils import module
from pyutils import saves


def start(name): print('START %s' % name.upper())

def end(name): print('END %s\n' % name.upper())


file.ensuredir('tests')
file.clear_directory('tests')


if False:

    start('FILE IO')
    file.writefile('test.txt', 'Test String')
    print(file.readfile('test.txt'))
    end('FILE IO')


if False:
    start('INITIALIZER')

    class TestClass:
        @initializer
        def __init__(self, var=0, **kwargs):
            pass

    test_class = TestClass(5, var2='hello, world!')
    print(test_class.var)
    print(test_class.var2)

    end('INITIALIZER')


if False:

    start('DICTS')

    print('Merge {{\'a\':\'b\'}} & {{\'c\': \'d\'}}: {}'.format(structure.dict.merge({'a': 'b'}, {'c': 'd'})))
    print("Flatten {{'a': 'b', 'c': {{'d': 'e'}}}}: {}".format(structure.dict.flatten({'a': 'b', 'c': {'d': 'e'}})))
    print("Update {{'a': {{'b': 'c', 'd': 'e'}}}} with {{'a': {{'b': 'f'}}}}: {}".format(structure.dict.update({'a': {'b': 'c', 'd': 'e'}}, {'a': {'b': 'f'}})))

    end('DICTS')


if False:

    start('STRUCT')

    d = {'a': 'b', 'c': 'd'}
    sd = structure.Struct(**d)
    print('{} -> {}'.format(d, sd))

    end('STRUCT')


if False:
    start('LISTS')

    print('Flatten [1, [2, [3]], 4, [5, 6, [[7]]]]: ', structure.list.flatten([1, [2, [3]], 4, [5, 6, [[7]]]]))

    end('LISTS')


if False:
    start('MODULE INSTALLER')

    module.pip.install_module('Pillow')
    import PIL

    end('MODULE INSTALLER')


if True:

    simple_data = {
        'key': 'val',
        'key2': 0,
        'key3': False,
        'key5': None
    }

    nested_data = {
        'a': 'b',
        'c': {
            'd': False,
            'e': 0,
            'f': [
                {'attr': 5}, {'attr': 7}, {'attr': 3}
            ]
        }
    }

    jsonfile = saves.JsonDataLoader('tests/test', indent=4)
    jsonfile.save(nested_data)
    print(jsonfile.load())

    simple_prop = saves.ProperyLoader('tests/test.prop')
    simple_prop.save(simple_data)
    print(simple_prop.load())

    plist = saves.PListLoader('tests/test')
    plist.save(nested_data)
    print(plist.load())
