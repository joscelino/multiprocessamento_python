from threading import Event, Thread
from time import sleep


def wait_set():
    sleep(3)
    event.set()


event = Event()
t = Thread(
    target=wait_set,
    name='Event',
    daemon=False
)
t.start()

print('antes')
event.wait()
print('depois')
