# file = open('test1.txt', 'r')

# # file.write('hello\n')
# # file.write('world')
# # file.writelines('hello')
# # file.write('hello ')
# # print(file.read())


# file.close()

# with open('test1.txt') as file:
#     print(file.read())

'''
JSON

сериалтизация(с Python в JSON) -> dump, dumps
десериализация(с JSON в Python) -> load, loads

'''

import json

# d = {'hello': True, 'age': 2, 'name': None}

# json_obj = json.dumps(d)
# print(json_obj) # {"hello": true, "age": 2, "name": null}

# python_obj = json.loads(json_obj)
# print(python_obj) # {'hello': True, 'age': 2, 'name': None}

with open('data.json', 'r') as file:
    # py_obj = json.loads(file.read()) # {'name': None}
    py_obj = json.load(file) # {'name': None}
    print(py_obj)

