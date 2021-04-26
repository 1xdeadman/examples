# https://docs.python.org/3/library/multiprocessing.html
import time
import multiprocessing as mp
import queue


print("lol will be with proccess")


def proc_func(my_queue: mp.Queue):
    for i in range(10):
        time.sleep(1)
        try:
            # put(obj[, block[, timeout]])
            try:
                my_queue.put(f"{i}: from {mp.current_process().name}", timeout=0.1)  # [block[, timeout]]
            except queue.Full:
                print('Queue is full')
            # if i <= 4 and not my_queue.full():
            #     my_queue.put(f"{i}: from {mp.current_process().name}", timeout=0.1)  # [block[, timeout]]
        except ValueError:
            print('Queue is closed')
            break
        if i == 4:
            my_queue.put("CLOSED!")
            my_queue.close()


if __name__ == '__main__':
    my_queue = mp.Queue(maxsize=32)
    prod_1 = mp.Process(
        target=proc_func,
        name="prod 1",
        args=(my_queue, )
    )
    prod_2 = mp.Process(
        target=proc_func,
        name="prod 2",
        args=(my_queue, )
    )
    prod_1.start()
    prod_2.start()
    closed_count = 0
    while my_queue:
        try:
            text = my_queue.get(block=False, timeout=0.1)
            if type(text) is str and len(text) > 0:
                print(text)  # [block[, timeout]]
                if text == "CLOSED!":
                    closed_count += 1
                if closed_count == 2:
                    print('END')
                    break
        except Exception as ex:
            print(ex)
    prod_1.join()
    prod_2.join()
    print(f"{prod_1.name} finished")
    print(f"{prod_2.name} finished")

# Listeners and Clients
# SimpleQueue
# JoinableQueue
