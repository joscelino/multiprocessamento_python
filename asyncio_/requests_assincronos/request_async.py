"""
Fazer download das imagens dos 100 primeiros pokemons da API

Tempo total (hh:mm:ss.ms) 0:00:01.835386

"""

import asyncio
from aiohttp import ClientSession
from aiofiles import open as aopen
from urllib.parse import urljoin
from requests import get
from contextlib import contextmanager
from datetime import datetime
from shutil import rmtree
from os.path import exists
from os import makedirs

path = 'downloads'
number = 100
BASE_URL = 'https://pokeapi.co/api/v2/'

if exists(path):
    rmtree(path)
makedirs(path)

pokemons = get(urljoin(base_url, f'pokemon/?limit={number}')).json()['results']


async def write_file(session, url, name, path):
    async with session.get(url) as response:
        print(f'Baixando: {name} - {url[-6:-4]}')
        async with aopen(f'{path}/{name}.jpg', 'wb') as f:
            content = await response.content.read()
            await f.write(content)


async def fetch(sem, session, url, name):
    async with sem:
        async with session.get(url) as response:
            result = await response.json()
            sprite_url = result['sprites']['front_default']
            # print(sprite_url)
            await write_file(session, sprite_url, name, path)


async def main():
    tasks = []
    sem = asyncio.Semaphore(number)

    async with ClientSession() as session:
        for pokemon in pokemons:
            url = pokemon['url']
            name = pokemon['name']
            # print(name, url)
            task = asyncio.ensure_future(fetch(sem, session, url, name))
            tasks.append(task)
        responses = asyncio.gather(*tasks)
        await responses


@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print('Tempo total (hh:mm:ss.ms) {}'.format(time_elapsed))


with timeit() as t:
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(main())
    loop.run_until_complete(future)
