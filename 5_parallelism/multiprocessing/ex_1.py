# https://docs.python.org/3/library/multiprocessing.html
'''
multiprocessing is a package that supports spawning processes using an
API similar to the threading module. The multiprocessing package offers
both local and remote concurrency, effectively side-stepping the Global
Interpreter Lock by using subprocesses instead of threads. Due to this,
the multiprocessing module allows the programmer to fully leverage multiple
processors on a given machine. It runs on both Unix and Windows.
'''
import time
import sys
import multiprocessing as mp

print("lol will be with proccess")


def show_proc_info():
    print("children:")
    for child in mp.active_children():
        print(f"-- {child}")
    print("cpu_count:", mp.cpu_count())
    # os.cpu_count()
    print("current_process:", mp.current_process())


def proc_func():
    if len(sys.argv) > 1:
        command = sys.argv[1]
    else:
        command = ""
    for i in range(10):
        time.sleep(1)
        print(f'{i}: {command}: {mp.current_process().name}')


if __name__ == '__main__':
    mp.freeze_support()
    new_process = mp.Process(target=proc_func, name="new_process")
    new_process.start()
    show_proc_info()
    proc_func()

    new_process.join()
    print(new_process.is_alive())
    print(new_process.pid)
    new_process.terminate()
    new_process.kill()
    new_process.close()
    print(f"{new_process.name} finished")
