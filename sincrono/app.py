"""
Fazer download das imagens dos 100 primeiros pokemons da API

Tempo total (hh:mm:ss.ms) 0:00:54.386109

"""
from contextlib import contextmanager
from datetime import datetime
from os import makedirs
from os.path import exists
from shutil import rmtree, copyfileobj
from urllib.parse import urljoin
from pprint import pprint
from requests import get

path = 'downloads'
base_url = 'https://pokeapi.co/api/v2/'


if exists(path):
    rmtree(path)
makedirs(path)


def download_file(name, url, *, path='downloads', type='png'):
    """Executa o download de um arquivo."""
    xpto = get(url, stream=True)
    with open(f'{path}/{name}.{type}', 'wb') as f:
        copyfileobj(xpto.raw, f)
    return f'{path}/{name}'


def get_sprite_url(url, sprite='front_default'):
    return get(url).json()['sprites'][sprite]


@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print('Tempo total (hh:mm:ss.ms) {}'.format(time_elapsed))


with timeit() as t:
    # Faz o request inicial da lista dos 100 primeiros pokemons
    pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']

    # Agora temos que entrar na url de cada pokemon para pegar a url da imagem
    images_url = {j['name']: get_sprite_url(j['url']) for j in pokemons}

    # Agora o download de cada uma das imagens
    files = [download_file(name, url) for name, url in images_url.items()]

pprint(files)
