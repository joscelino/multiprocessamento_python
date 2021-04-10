"""
Tempo total (hh:mm:ss.ms) 0:00:15.057766

"""
from urllib.parse import urljoin
from multiprocessing import Pool
from requests import get
from functions import target, timeit


base_url = 'https://pokeapi.co/api/v2/'


def get_urls():
    """Faz o get das urls."""
    return get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']


if __name__ == '__main__':

    with timeit():
        poke = get_urls()
        with Pool(10) as workers:
            result = workers.map(target, poke)
            result_2 = workers.map(target, poke)
