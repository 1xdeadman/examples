from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def encrypt(
            self,
            text_filename: str,
            key_filename: str,
            **args) -> bool:
        '''
        шифрование файла по ключу

        text_filename -- имя файла для зашифрования
        key_filename -- имя файла ключа
        '''
        pass

    @abstractmethod
    def decrypt(
            self,
            encrypted_filename: str,
            key_filename: str,
            **args) -> bool:
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

    def _read_text(self, text_filename: str) -> bool:
        """общий метод для чтения текстового файла"""
        pass


class GammEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(
            self,
            text_filename: str,
            key_filename: str,
            **args) -> bool:
        pass

    def decrypt(
            self,
            encrypted_filename: str,
            key_filename: str,
            **args) -> bool:
        pass

    def gen_key(self, **args) -> bool:
        pass

    def _read_encrypt(self, encrypted_filename: str) -> bool:
        """прочитать защифрованный файл

        encrypted_filename -- имя файла для чтения
        """
        pass

    def _read_key(self, key_filename: str) -> bool:
        """метод для чтения ключа

        key_filename -- имя файла для чтения
        """
        pass


class ReplaceEncrypt(MyAbstractClass):
    def __init__(self):
        pass

    def encrypt(
            self,
            text_filename: str,
            key_filename: str,
            **args) -> bool:
        pass

    def decrypt(
            self,
            encrypted_filename: str,
            key_filename: str,
            **args) -> bool:
        pass

    def gen_key(self, **args) -> bool:
        pass

    def _read_encrypt(self, encrypted_filename: str) -> bool:
        """прочитать защифрованный файл

        encrypted_filename -- имя файла для чтения
        """
        pass

    def _read_key(self, key_filename: str) -> bool:
        """метод для чтения ключа

        key_filename -- имя файла для чтения
        """
        pass


obj_rep = ReplaceEncrypt()
obj_gam = GammEncrypt()
