"""
Tempo total (hh:mm:ss.ms) 0:00:57.900427

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
base_url = 'https://pokeapi.co/api/v2/'

if exists(path):
    rmtree(path)
makedirs(path)

pokemons = get(urljoin(base_url, 'pokemon/?limit=100')).json()['results']


async def write_file(session, url, name, path):
    async with session.get(url) as response:
        print(f'Baixando: {name}')
        async with aopen(f'{path}/{name}.jpg', 'wb') as f:
            content = await response.content.read()
            await f.write(content)


async def fetch(session, url):
    async with session.get(url) as response:
        result = await response.json()
        sprite_url = result['sprites']['front_default']
        # print(sprite_url)
        return sprite_url


async def main():
    async with ClientSession() as session:
        for pokemon in pokemons:
            url = pokemon['url']
            name = pokemon['name']
            # print(name, url)
            result = await fetch(session, url)
            await write_file(session, result, name, path)


@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print('Tempo total (hh:mm:ss.ms) {}'.format(time_elapsed))


with timeit() as t:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
