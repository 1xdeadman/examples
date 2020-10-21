# https://docs.python.org/3/library/multiprocessing.html
import time
import multiprocessing as mp

print("lol will be with proccess")


def proc_func(my_pipe):
    try:
        for i in range(10):
            time.sleep(1)
            my_pipe.send(f"{i}: from {mp.current_process().name}")
            if i == 7:
                my_pipe.send("CLOSED")
                break
    except OSError as xe:
        print("Pipe was closed")


if __name__ == '__main__':
    first_dialog_pipe, second_dialog_pipe = mp.Pipe(duplex=True)
    new_process = mp.Process(
        target=proc_func,
        name="new_process",
        args=(second_dialog_pipe, )
    )

    new_process.start()

    try:
        while True:
            if first_dialog_pipe.poll(0.2):
                print('data:', end=' ')
                text = first_dialog_pipe.recv()
                print(text)
                if text == "CLOSED":
                    break
            else:
                print('--')
    except EOFError:
        print("END")

    new_process.join()
    print(f"{new_process.name} finished")

# Listeners and Clients
