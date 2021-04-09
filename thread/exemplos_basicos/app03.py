import threading
from time import sleep


def wait():
    sleep(2)


class myThread(threading.Thread):
    def __init__(self, target, name='MyThread'):
        super().__init__()
        self.target = target
        self.name = name

    def run(self) -> None:
        self.target()


t = myThread(wait)
t.start()
print(t.name)
