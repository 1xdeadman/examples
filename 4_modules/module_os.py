# https://docs.python.org/3/library/os.html
import os


def show(name, info):
    print()
    print(name, info)


def get_os_info():
    show("getlogin:", os.getlogin())  # Unix, Windows


def fylesystem_spec_symbols():
    print("curdir:", os.curdir)
    print("pardir:", os.pardir)
    print("sep:", os.sep)
    print("altsep:", os.altsep)
    print("extsep:", os.extsep)
    print("pathsep:", os.pathsep)
    print("defpath:", os.defpath)
    print("linesep:", os.linesep)


def work_with_environment():
    show("name:", os.name)
    show("environ(PATH):", os.environ['PATH'])
    show("getenv(PATH):", os.getenv('huhuh'))  # Unix, Windows
    show("get_exec_path():", os.get_exec_path())


def get_filesystem_info():
    my_path = '.'
    show("listdir", os.listdir(path=my_path))
    print("scandir:")
    for elem in os.scandir(my_path):
        print("     name -", elem.name)
        print("         path -", elem.path)
        print("         inode -", elem.inode())
        print("         is_dir -", elem.is_dir())
        print("         is_file -", elem.is_file())
        print("         is_symlink -", elem.is_symlink())
        print("         stat -", elem.stat())


def path_info_func():
    print("abspath:", os.path.abspath("."))
    print("basename:", os.path.basename("D:/projects/AuthServer/AuthServer/bin/Release/netcoreapp3.1/AuthServer.dll"))
    print("dirname:", os.path.dirname("D:\\projects\\"))
    print("commonpath:", os.path.commonpath(["D:/projects/AuthServer", "D:\\projects\\CDO", "D:/projects/MarkerInfrastructure"]))
    print("commonprefix:", os.path.commonprefix(["E:/projects/AuthServer", "D:/projects\\CDO", "D:/projects/MarkerInfrastructure"]))
    print("getatime:", os.path.getatime(r"D:\projects\studies\statistics\data.txt"))
    print("getmtime:", os.path.getmtime(r"D:\projects\studies\statistics\data.txt"))
    print("getctime:", os.path.getctime(r"D:\projects\studies\statistics\data.txt"))
    print("getsize:", os.path.getsize(r"D:\projects\studies\statistics\data.txt"))  # bytes
    print("isabs:", os.path.isabs(r"D:\projects\studies\statistics\data.txt"))
    print("join:", os.path.join("asd", "sad", "qwe"))
    print("normcase:", os.path.normcase("D://projects//web//AuthServer"))
    print("normpath:", os.path.normpath("D://projects//web//AuthServer"))
    print("samefile:", os.path.samefile("D:/projects/web/AuthServer", "D:/projects/web/AuthServer"))
    print("split:", os.path.split("D:/projects/web/AuthServer"))
    print("splitdrive:", os.path.splitdrive("D:/projects/web/AuthServer"))
    print("splitext:", os.path.splitext(r"D:\projects\studies\statistics\data.txt"))


def work_with_filesystem():
    base_path = os.getcwd()
    show("getcwd:", os.getcwd())
    os.chdir(base_path + "/Data")
    show("getcwd:", os.getcwd())

    # существует ли директория или файл
    if os.path.exists(base_path + "/modules") is True:
        print("modules")
    if(os.path.isdir("dir1") is False):  # существует ли директория "mem"
        os.mkdir("dir1")  # создать директорию
        # создает рекурсивно директории
        os.makedirs("dir1/dir2/dir3/dir4")
    if(os.path.isfile("files.py") is True):  # существует ли файл "files.py"
        print("files.py is file")
    # os.rmdir("dir1")  # удалить директорию
    # os.removedirs("dir1/dir2/dir3/dir4")  # удалить директории рекурсивно
    open("test", "w")
    if(os.path.isfile("test") is True):
        pass
        # os.chmod("test", 7)  # изменить права на чтение/запись/выполнение
        # os.remove("test")  # удалить файл

    a = os.open("ddd", os.O_CREAT)
    show("open:", a)
    os.close(a)

    if os.path.exists('xxx') is True:
        os.remove('xxx')

    os.rename('ddd', 'xxx')  # переименовать файл или директорию

    a = open("test", "+wb")
    a.write(b'asds')
    a.close()

    show("stat:", os.stat("test"))
    # заменить содержимое файла xxx файлом test. Файл test удаляется.
    os.replace('test', 'xxx')
    # создать ссылку. Требует админских прав.
    # os.symlink("E:/projects/examples/Data/text.txt", "lololo")


# get_os_info()
# fylesystem_spec_symbols()
# work_with_environment()
# get_filesystem_info()
path_info_func()
# work_with_filesystem()
