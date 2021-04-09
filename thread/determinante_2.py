from threading import Thread, Event
from queue import Queue
from functools import reduce
from time import sleep

q = Queue(maxsize=2)
r = Queue()
e = Event()

matriz = [[3, 9],
          [3.5, -6]]


def principal(mat):
    sleep(10)
    q.put(mat[0][0] * mat[1][1])


def secundaria(mat):
    count = 0
    while q.empty():
        count += 1

    print(count)
    q.put(mat[1][0] * mat[0][1])
    e.set()


def result():
    e.wait()
    r.put(
        reduce(
            lambda x, y: x - y,
            q.queue
        )
    )


t_p = Thread(
    target=principal,
    kwargs={'mat': matriz},
    name='principal',
    daemon=True
)
t_p.start()

t_s = Thread(
    target=secundaria,
    kwargs={'mat': matriz},
    name='secudaria',
    daemon=True
)

t_s.start()

t_r = Thread(
    target=result,
    name='result',
    daemon=True
)

t_r.start()
t_r.join()

print(r.queue[0])
