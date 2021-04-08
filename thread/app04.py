from threading import Thread, Lock

c = 0
lock = Lock()


def count_300():
    global c
    lock.acquire()
    try:
        while c < 300:
            c += 1
            print(c)
    finally:
        lock.release()


def count_1000():
    global c
    c = 400
    while c < 1000:
        c += 1
    print(c)


t_0 = Thread(target=count_300, name='300', daemon=True)
t_0.start()
t_1 = Thread(target=count_1000, name='100', daemon=False)
t_1.start()
