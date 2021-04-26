# https://docs.python.org/3/library/threading.html
'''
The Thread class represents an activity that isrun in a separate thread of control.
There are two ways to specify the activity:
by passing a callable object to the constructor, or by overriding the run() method in a subclass.
No other methods (except for the constructor) should be overridden in a subclass.
In other words, only override the __init__() and run() methods of this class.
'''


import threading
import time

print("lol will be with proccess")


def show_threads_info():
    print("threads_info:")
    print(f"-active threads: {threading.active_count()}")  # получить число запущенных потоков
    print(f"-main thread: {threading.main_thread()}")  # получить объект управления основным потоком
    print("-threads list: ")
    for thread in threading.enumerate():  # получить список всех объектов управления запущенных потоков
        print("--", thread.name, thread.ident)  # через name можно получить имя потока, ident - числовой идентификатор
    print()


def show_cur_thread_info():
    print("cur_thread_info:")
    print(f"-current_thread: {threading.current_thread()}")  # получить объект текущего потока
    print(f"-cur_thread_id: {threading.get_ident()}")  # получить идентификатор текущего потока


def thread_func(lol: str):
    show_cur_thread_info()
    for i in range(10):
        time.sleep(1)  # поток, в котором вызвана функция sleep приостанавливается на указанное количество секунд
        print(f"{i}: {threading.get_ident()}")  # получить идентификатор текущего потока


def ex_1():
    print("ex_1")
    # создание объекта управления потоком
    thread_lol = threading.Thread(
        target=thread_func,  # функция, с которой начнется выполнение потока
        name="name",  # имя, присваиваемое потоку
        kwargs={"lol": "kek"}  # аргументы, передаваемые в стартовую функцию потока
    )
    print(f"thread_lol is started: {thread_lol.is_alive()}")  # метод is_alive возвращает True, если поток запущен
    thread_lol.start()  # запуск потока. С этого момента поток начнет выполнять код
    time.sleep(0.5)  # поток, в котором вызвана функция sleep приостанавливается на указанное количество секунд
    show_threads_info()
    time.sleep(2)
    print(f"thread_lol is started: {thread_lol.is_alive()}")
    thread_lol.join()  # при вызове этого метода поток, в  будет ожидание, что поток завершится
    # thread_lol.join(5.0)  # время ожидания завершения. При превышении - выполнение ожидающего потока продолжится
    print(f"thread_lol is started: {thread_lol.is_alive()}")
    print("exit")
    # or
    # print(f"thread_lol is started: {thread_lol.is_alive()}")


if __name__ == "__main__":
    ex_1()
