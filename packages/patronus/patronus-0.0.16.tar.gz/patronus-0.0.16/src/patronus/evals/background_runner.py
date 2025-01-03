import asyncio
import threading
from concurrent.futures import Executor, ThreadPoolExecutor
from typing import Callable, Optional, Any


class EvaluationsBackgroundRunner:
    def __init__(self, *, loop: Optional[asyncio.AbstractEventLoop]=None, executor: Optional[Executor]=None):
        self._loop = loop or asyncio.get_event_loop_policy().new_event_loop()
        self._executor = executor or ThreadPoolExecutor()

        self._thread = threading.Thread(
            target=self._run_loop,
            # We don't want to close the thread abruptly, on program exit.
            # When program exists we try to finish pending requests and do cleanup.
            daemon=False,
        )
        self._thread.start()

    def _run_loop(self) -> None:
        asyncio.get_event_loop_policy().set_event_loop(self._loop)
        self._loop.run_forever()
        self._loop.close()

    def submit(self, fn: Callable[..., Any], *args: Any, **kwargs: Any) -> None:
        if asyncio.iscoroutinefunction(fn):
            coro = fn(*args, *kwargs)
            asyncio.run_coroutine_threadsafe(coro, loop=self._loop)
        self._loop.run_in_executor(self._executor, fn, args, kwargs)

    def shutdown(self) -> None:
        self._loop.stop()
        self._thread.join()