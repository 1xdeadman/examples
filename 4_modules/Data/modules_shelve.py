# off docs - https://docs.python.org/3/library/shelve.html

import shelve

filename = "TestData/shelve/db.shelve"
'''
'r' - Open existing database for reading only (default)
'w' - Open existing database for reading and writing
'c' - Open database for reading and writing, creating it if it doesn’t exist
'n' - Always create a new, empty database, open for reading and writing
'''

key = 'key'
d = shelve.open(filename)  # writeback=True

d[key] = 123
data = d[key]

print("data:", data)

del d[key]

print(d.get(key))
flag = key in d

print(list(d.keys()))

d['xx'] = [0, 1, 2]
d['xx'].append(3)
print(d['xx'])

temp = d['xx']
temp.append(5)
d['xx'] = temp

d.sync()
d.close()
