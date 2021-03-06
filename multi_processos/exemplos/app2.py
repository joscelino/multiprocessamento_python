"""Criacao de worker com API similas as Threads"""

from multiprocessing import Process
from os import getpid


class Worker(Process):
    def __init__(self, target, *, name):
        super().__init__()
        self.name = name
        self.target = target

    def run(self) -> None:
        self.target(self.name, getpid())


w1 = Worker(target=print, name='Processo 1')
w2 = Worker(target=print, name='Processo 2')
w3 = Worker(target=print, name='Processo 3')

if __name__ == '__main__':

    w1.start()
    w2.start()
    w3.start()

    w1.join()
    w2.join()
    w3.join()
