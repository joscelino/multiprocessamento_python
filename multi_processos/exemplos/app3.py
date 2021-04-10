"""Ideia de funcoes nao serializaveis."""

from pickle import dumps
from multiprocessing import Process


def closure(func):
    """A funcao (func) esta no escopo da closure."""
    def inner(*args):
        return print(func(*args))
    return inner


@closure
def add(x, y):
    return x + y


if __name__ == '__main__':
    p = Process(
        target=add,
        args=(7, 7),
    )
    print(dumps(add))
    p.start()
    p.join()
