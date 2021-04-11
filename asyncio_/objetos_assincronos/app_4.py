from asyncio import ensure_future, gather, get_event_loop, sleep
from collections.abc import AsyncIterator
from functools import singledispatch
from types import coroutine
from typing import Collection, Dict, Union


@singledispatch
@coroutine
def aiter(iterator: Union[Collection, Dict]):
    pass


@aiter.register(Collection)
@coroutine
def col_aiter(iterator):
    yield from iterator


@aiter.register(Dict)
@coroutine
def col_aiter(iterator):
    yield from iterator.items()


class AsyncCollection(AsyncIterator):
    def __init__(self, col: Union[Collection, Dict], *, loop=None):
        self._iterator = aiter(col)
        self._loop = loop or get_event_loop()

    def __aiter__(self):
        return self

    async def __anext__(self):
        value = await self._loop.run_in_executor(
            None, next, self._iterator, self
        )
        if value is self:
            raise StopAsyncIteration
        return await sleep(0.1, result=value)


list_1 = 'bananas'
list_2 = list(range(9))
dict_1 = {1: 'Good', 2: 'Look'}


async def run_loop(obj):
    async for val in AsyncCollection(obj):
        print(val)


async def main():
    future_1 = ensure_future(run_loop(list_1))
    future_2 = ensure_future(run_loop(list_2))
    furture_3 = ensure_future(run_loop(dict_1))

    result = gather(future_1, future_2, furture_3)
    await result


loop = get_event_loop()
loop.run_until_complete(main())