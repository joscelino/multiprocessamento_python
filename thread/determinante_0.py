from threading import Thread
from queue import Queue

q = Queue()

matriz = [[3, 9],
          [3.5, -6]]


def principal(mat):
    q.put(mat[0][0] * mat[1][1])


def secundaria(mat):
    count = 0
    while q.empty():
        count += 1

    print(count)
    q.put(mat[1][0] * mat[0][1])


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

t_s.join()

val_p = q.queue[0]
val_s = q.queue[1]
print(f'Determinante: {val_p - val_s}')
