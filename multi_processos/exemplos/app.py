"""Exemplo de como compartilhar uma queue entre processos e threads"""

from collections import namedtuple
from threading import Thread
from multiprocessing import Process, Queue
from os import getpid, getppid
# from queue import Queue


q = Queue()
pstate = namedtuple('pstate', 'name pid ppid')


def info(name):
    obj = pstate(name, getpid(), getppid())
    print(obj)
    q.put(obj)


info('main line')

t = Thread(
    target=info,
    args=('Thread',),
)
p = Process(
    target=info,
    args=('Process',)
)


if __name__ == "__main__":

    t.start()
    p.start()

    t.join()
    p.join()

    # print(q.queue)
    print([q.get() for e in range(2)])
