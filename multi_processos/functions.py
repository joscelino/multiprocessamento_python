from shutil import copyfileobj, rmtree
from contextlib import contextmanager
from datetime import datetime
from os.path import exists
from os import makedirs
from requests import get

path = 'downloads'

if exists(path):
    rmtree(path)
makedirs(path)


def get_bin_file(args):
    name, url = args
    return name, get(url, stream=True).raw


def get_sprite_url(url, sprite='front_default'):
    return url['name'], get(url['url']).json()['sprites'][sprite]


def save_file(args, path=path, type='png'):
    """Salva o binario no disco como imagem"""
    name, binary = args
    fname = f'{path}/{name}.{type}'
    with open(fname, 'wb') as f:
        copyfileobj(binary, f)


class Pipeline:
    def __init__(self, *funcs):
        self.funcs = funcs

    def __call__(self, argument):
        state = argument
        for func in self.funcs:
            state = func(state)
        return state


target = Pipeline(get_sprite_url, get_bin_file, save_file)


@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print('Tempo total (hh:mm:ss.ms) {}'.format(time_elapsed))
