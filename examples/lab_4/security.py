"""
Реализуете в этом модуле механизмы:
1) шифрования/расшифрования данных
2) хеширования данных
3) генерации ключей

https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password
https://pypi.org/project/pycryptodome/
https://www.pycryptodome.org/en/latest/src/api.html
https://docs.python.org/3/library/hashlib.html
"""

from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import random


_IV456 = b'yo_esK1DOHg2x-3L'  # 16 байт
_SALT = b'8_TuDUK9IpJKaM7NWkpSQcMlVh0ZoEmYdeIOjvItOSk='
_LEN_BLOCK_SIZE = 16


def gen_user_secret_key(password: bytes) -> bytes:
    if isinstance(password, bytes) is False:
        raise TypeError(r"isinstance(password, bytes) is False")
    res = hashlib.pbkdf2_hmac(
        'sha256',
        password,
        _SALT,
        100000)
    return res


def hash_value(value: bytes) -> str:
    if isinstance(value, bytes) is False:
        raise TypeError(r"isinstance(value, bytes) is False")
    m = hashlib.sha256(_SALT + value)
    hashed_pas = m.hexdigest()
    return hashed_pas


def _fill_random_bytes(bytes_str: bytes, length: int) -> bytes:
    while len(bytes_str) % length != 0:  # должно быть кратно 16 байт
        symbol = bytes()
        if len(bytes_str) > 0:
            pos = random.randint(0, len(bytes_str))
            symbol = bytes_str[pos: pos + 1]
        bytes_str += symbol
    return bytes_str


def encrypt(message: bytes, key: bytes) -> bytes:
    if isinstance(message, bytes) is False:
        raise TypeError(r"isinstance(message, bytes) is False")
    if isinstance(key, bytes) is False:
        raise TypeError(r"isinstance(key, bytes) is False")

    len_block = len(message).to_bytes(length=_LEN_BLOCK_SIZE, byteorder='big')
    message = len_block + message
    # должно быть кратно 16 байт
    message = _fill_random_bytes(message, _LEN_BLOCK_SIZE)
    obj = AES.new(key, AES.MODE_CBC, _IV456)
    ciphertext = obj.encrypt(message)

    return ciphertext


def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    if isinstance(ciphertext, bytes) is False:
        raise TypeError(r"isinstance(ciphertext, bytes) is False")
    if isinstance(key, bytes) is False:
        raise TypeError(r"isinstance(key, bytes) is False")
    if len(ciphertext) % _LEN_BLOCK_SIZE != 0:
        raise ValueError(r"len(bytes_str) % length != 0")

    # ciphertext = _fill_random_bytes(ciphertext, _LEN_BLOCK_SIZE)

    obj = AES.new(key, AES.MODE_CBC, _IV456)
    text = obj.decrypt(ciphertext)

    size = int.from_bytes(text[:_LEN_BLOCK_SIZE], byteorder='big')
    text = text[_LEN_BLOCK_SIZE:size + _LEN_BLOCK_SIZE]

    return text


def gen_secret_key() -> bytes:
    # длина ключа AES равна 16, 24, или 32 байтам.
    return Random.new().read(32)


if __name__ == "__main__":
    pass
    # print(SHA256.new("1".encode(encoding='utf-8')).hexdigest())
    # или
    # print(hashlib.sha256("1".encode(encoding='utf-8')).hexdigest())
