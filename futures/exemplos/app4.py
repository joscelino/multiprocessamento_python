from concurrent.futures import ProcessPoolExecutor, as_completed
from time import sleep

l_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def ident(x):
    return x


if __name__ == '__main__':

    with ProcessPoolExecutor() as exec:
        """
        GIL: tarefas bloqueantes de I/O vao dar bypass no GIL
        """
        l_futures = []

        for e in l_ints:
            worker = exec.submit(ident, e)
            l_futures.append(worker)

        for worker in as_completed(l_futures):
            resp = worker.result()
            print(worker, resp)
