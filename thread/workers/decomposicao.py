"""
Fazer download das imagens dos 100 primeiros pokemons da API

Tempo total (hh:mm:ss.ms) 0:00:06.469827

"""

from threading import Event, Thread
from queue import Queue
from time import sleep
from urllib.parse import urljoin
from requests import get
from functions import target, timeit

BASE_URL = 'https://pokeapi.co/api/v2/'
event = Event()
queue = Queue(maxsize=101)


def get_urls():
    pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']
    [queue.put(pokemon) for pokemon in pokemons]
    event.set()
    queue.put('Kill')


class Worker(Thread):
    def __init__(self, target, queue, *, name='Worker'):
        super().__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self._stoped = False
        print(self.name, 'started.')

    def run(self) -> None:
        event.wait()
        while not self.queue.empty():
            pokemon = self.queue.get()
            print(self.name, pokemon)
            if pokemon == 'Kill':
                self.queue.put(pokemon)
                self._stoped = True
                break
            self._target(pokemon)

    def join(self):
        while not self._stoped:
            sleep(0.1)


def get_pool(n_th: int):
    """Retorna um numero n de Threads."""
    return [Worker(target=target, queue=queue, name=f'Worker_{n}')
            for n in range(n_th)]


with timeit():
    get_urls()
    thrs = get_pool(10)
    [th.start() for th in thrs]
    [th.join() for th in thrs]
