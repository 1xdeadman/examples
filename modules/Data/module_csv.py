"""
off docs: https://docs.python.org/3/library/csv.html
PEP – 305: https://www.python.org/dev/peps/pep-0305/
quick guide: https://metanit.com/python/tutorial/4.3.php
"""

import csv
from pprint import pprint
import os


def prelaunch_task(filename: str):
    if os.path.isfile(filename) is True:
        os.remove(filename)
    else:
        path = os.path.dirname(filename)
        if os.path.isdir(path) is False:
            os.makedirs(path)


def write_file(filename: str):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)  # , delimiter='/', quotechar='|'
        writer.writerow([1, "text data", ["sub str", 123]])
        writer.writerows([
            [1, "text data", ["sub str", 123]],
            [1, 2, 3],
            [True],
            [55]
        ])


def read_file(filename: str) -> list:
    res = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)  # ,  delimiter='/', quotechar='|'
        for line in reader:
            res.append(line)
    pprint(res)
    return line


def write_dict(filename: str):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["One", "Two", 3]  # , extrasaction='raise'
        )
        writer.writerow({
            "One": 123,
            "Two": "kek",
            3: [1, 2, 3]
        })
        writer.writerows([{
            "One": 123,
            "Two": "kek",
            3: [1, 2, 3]
        }, {
            "One": 222,
            "Two": "lol",
            3: [4, 5, 6]
        }])


def read_dict(filename: str) -> list:
    res = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(
            file,
            fieldnames=["One", "Two", 3]
        )
        for line in reader:
            res.append(dict(line))
    pprint(res)
    return line


TEST = 2
filename = "TestData/test.csv"
prelaunch_task(filename)
if TEST == 1:
    write_file(filename)
    read_file(filename)
elif TEST == 2:
    write_dict(filename)
    read_dict(filename)

# csv.Error
