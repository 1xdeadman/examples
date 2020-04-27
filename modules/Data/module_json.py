"""
off docs - https://docs.python.org/3/library/json.html
quick guide - https://pythonworld.ru/moduli/modul-json.html
"""
import json
import os


'''
Python ------ JSON
dict -------- object
list, tuple - array
str --------- string
int, float -- number
True  ------- true
False ------- false
None -------- null
'''


def prelaunch_task(filename: str):
    if os.path.isfile(filename) is True:
        os.remove(filename)
    else:
        path = os.path.dirname(filename)
        if os.path.isdir(path) is False:
            os.makedirs(path)


def write_json(filename: str):
    '''
    separators=('; ', '| ')
    default
    skipkeys
    ensure_ascii
    check_circular
    allow_nan
    '''
    data = {"One": 1, "Two": 2, 3: "Three"}
    with open(filename, 'w') as file:
        json.dump(data, file)


def read_json(filename: str):
    '''
    object_hook
    object_pairs_hook
    '''
    data = {}
    with open(filename, 'r') as file:
        data = json.load(file)
    print(data)


class MyClass():
    def __init__(self):
        self.x = 123
        self.value_2 = "Nani?!"


def my_encoder(data):
    if isinstance(data, MyClass) is True:
        return data.__dict__
    return None


def my_decoder(data):
    res = MyClass()
    res.x = data['x']
    res.value_2 = data['value_2']
    return res


def write_custom_json(filename: str):
    data = MyClass()
    with open(filename, 'w') as file:
        json.dump(data, file, default=my_encoder)


def read_custom_json(filename: str):
    data = {}
    with open(filename, 'r') as file:
        data = json.load(file, object_hook=my_decoder)
    print(data.x)


class MyClassEncoder(json.JSONEncoder):

    def default(self, o) -> dict:
        if isinstance(o, MyClass) is True:
            return {"x": o.x, "value_2": o.value_2}
        # raise TypeError("cann't conver to json")
        return json.JSONEncoder.default(self, o)


class MyClassDecoder(json.JSONDecoder):

    def decode(self, o: str) -> MyClass:
        print(o)
        if o.find('"x"') is not None:
            return MyClass()
        # raise TypeError("cann't conver from json")
        return json.JSONDecoder.decode(self, o)


def write_custom_json_2(filename: str):
    data = MyClass()
    with open(filename, 'w') as file:
        json.dump(data, file, cls=MyClassEncoder)


def read_custom_json_2(filename: str):
    data = {}
    with open(filename, 'r') as file:
        data = json.load(file, cls=MyClassDecoder)
    print(data)


TEST = 2
filename = "TestData/test.json"
prelaunch_task(filename)
if TEST == 1:
    write_json(filename)
    read_json(filename)
elif TEST == 2:
    write_custom_json(filename)
    read_custom_json(filename)
elif TEST == 3:
    write_custom_json_2(filename)
    read_custom_json_2(filename)


# json.JSONDecodeError
