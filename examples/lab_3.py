from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def encrypt(self, text_filename: str, key_filename, **args) -> bool:
        '''
        шифрование файла по ключу

        text_filename -- имя файла для зашифрования
        key_filename -- имя файла ключа
        '''
        pass

    @abstractmethod
    def decrypt(self, encrypted_filename: str, key, **args) -> bool:
        '''
        расшифрование файла по ключу

        encrypted_filename -- имя файла для расшифрования
        key_filename -- имя файла ключа
        '''
        pass

    @abstractmethod
    def gen_key(self, **args) -> bool:
        """генерация ключа"""
        pass

    def _read_text(self):
        """общий метод для чтения текстового файла"""
        pass


class GammEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(self, filename: str, key, **args) -> bool:
        pass

    def decrypt(self, filename: str, key, **args) -> bool:
        pass

    def gen_key(self, **args) -> bool:
        pass

    def _read_encrypt(self):
        """прочитать защифрованный файл"""
        pass

    def _read_key(self):
        """метод для чтения ключа"""
        pass


class ReplaceEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(self, filename: str, key, **args) -> bool:
        pass

    def decrypt(self, filename: str, key, **args) -> bool:
        pass

    def gen_key(self, **args) -> bool:
        pass

    def _read_encrypt(self):
        """прочитать защифрованный файл"""
        pass

    def _read_key(self):
        """метод для чтения ключа"""
        pass


obj_rep = ReplaceEncrypt()
obj_gam = GammEncrypt()
