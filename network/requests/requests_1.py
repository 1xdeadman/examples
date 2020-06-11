# https://requests.readthedocs.io/en/master/
# https://pypi.org/project/requests/

import requests


def ex_1():
    r = requests.get('https://requests.readthedocs.io/en/master/')
    print(r.status_code)
    print(r.url)
    print(r.encoding)
    if input("show headers?(Y/N)").lower() == "y":
        print(r.headers)
    if input("show text?(Y/N)").lower() == "y":
        print(r.text)

def ex_2():
    r = requests.get('http://localhost:8000/')
    print(r.status_code)
    print(r.url)
    print(r.encoding)
    if input("show headers?(Y/N)").lower() == "y":
        print(r.headers)
    if input("show text?(Y/N)").lower() == "y":
        print(r.text)

def ex_3():
    token = b''
    with open('jwt.token', 'rb') as jwt_token:
        token = jwt_token.read()
    print(token)
    headers = {
        "Authorization":  b"Bearer " + token
    }
    r = requests.get('http://localhost:8000/auth', headers=headers)
    print(r.status_code)
    print(r.url)
    print(r.encoding)
    if input("show headers?(Y/N)").lower() == "y":
        print(r.headers)
    if input("show text?(Y/N)").lower() == "y":
        print(r.text)
if __name__ == "__main__":
    ex_3()
