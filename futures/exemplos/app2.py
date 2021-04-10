from concurrent.futures import ThreadPoolExecutor
from time import sleep

with ThreadPoolExecutor(max_workers=2) as exec:
    """
    GIL: tarefas bloqueantes de I/O vao dar bypass no GIL
    """
    result_0 = exec.submit(sleep, 10)
    result_1 = exec.submit(print, 'Thread')
    print(result_0)
    print(result_1)
