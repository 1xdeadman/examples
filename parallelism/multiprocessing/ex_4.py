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
import multiprocessing as mp

print("lol will be with proccess")


def proc_func(my_pipe):
    for i in range(10):
        time.sleep(1)
        my_pipe.send(f"{i}: from {mp.current_process().name}")
        if i == 7:
            my_pipe.close()


if __name__ == '__main__':
    parent_dialog_pipe, child_dialog_pipe = mp.Pipe()
    new_process = mp.Process(
        target=proc_func,
        name="new_process",
        args=(child_dialog_pipe, )
    )

    new_process.start()

    while not parent_dialog_pipe.closed:
        print(parent_dialog_pipe.recv())

    new_process.join()
    print(f"{new_process.name} finished")

# Listeners and Clients
