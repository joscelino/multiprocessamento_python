import threading
from time import sleep


def wait():
    sleep(2)


t1 = threading.Thread(
    target=wait,
    name='Wait-Deamon',
    daemon=True
)

t2 = threading.Thread(
    target=wait,
    name='Wait',
    daemon=False
)


t1.start()
t2.start()

print(t1.is_alive())
print(t1.name)
print(t2.is_alive())
print(t2.name)
