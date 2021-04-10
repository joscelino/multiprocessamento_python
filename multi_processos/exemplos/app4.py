"""Exemplo de Pool nativo"""

from multiprocessing import Pool
from os import getpid
from pprint import pprint


def soma_2(x):
    return x + 2, getpid()


if __name__ == '__main__':

    workers = Pool(5)

    # Sync
    # result = workers.map(soma_2, range(100))
    # pprint(result)

    # Async
    result = workers.map_async(soma_2, range(100))
    result.wait()
    pprint(result.get())
