from concurrent.futures import ProcessPoolExecutor, as_completed
from functools import partial
from time import sleep

if __name__ == '__main__':

    with ProcessPoolExecutor() as exec:
        """
        GIL: tarefas bloqueantes de I/O vao dar bypass no GIL
        """
        result_0 = exec.submit(sleep, 5)
        result_1 = exec.submit(print, 'Comecou')
        print(result_0)
        print(result_1)
        result_0.add_done_callback(partial(print, 'Terminou!'))
