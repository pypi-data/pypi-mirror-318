import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable


def run_async_in_executor(coroutine_func: Callable[[], Any]) -> Any:
    """
    A unified method for async execution for more efficient and safer thread management

    Arguments:
        coroutine_func {Callable[[], Any]} -- The coroutine to run

    Returns:
        Any -- The result of the coroutine
    """

    def run_async_in_thread():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(coroutine_func())
        loop.close()
        return result

    with ThreadPoolExecutor() as executor:
        future = executor.submit(run_async_in_thread)
        return future.result()
