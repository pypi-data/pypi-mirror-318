import asyncio
import functools
import random
import threading
from concurrent.futures.thread import ThreadPoolExecutor

finished = 0
exs = 0

async def dummy_2(x):
    global finished
    finished += 1
    return x + 2

async def dummy(x):
    if random.random() < 0.01:
        global exs
        exs += 1
        raise ValueError("??")
    global finished
    finished += 1
    return (await dummy_2(x)) + 1


class Runner:
    def __init__(self):
        self.loop = asyncio.get_event_loop_policy().new_event_loop()
        self.executor = ThreadPoolExecutor()
        self.thread = threading.Thread(
            target=self._run_loop,
            daemon=False,
        )
        self.thread.start()
        print("Running...", flush=True)

    def _run_loop(self):
        self.loop.run_forever()
        print(f"run_forever stopped, finished: {finished}", flush=True)
        tasks = asyncio.all_tasks(self.loop)
        if tasks:
            self.loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
            print(f"run_until_completed, finished: {finished}", flush=True)
        self.loop.close()
        print(f"excs: {exs}", flush=True)


    def submit(self, fn, *args, **kwargs):
        if asyncio.iscoroutinefunction(fn):
            asyncio.run_coroutine_threadsafe(fn(*args, **kwargs), self.loop)
        else:
            asyncio.run_coroutine_threadsafe(functools.partial(self.loop.run_in_executor, fn, args, kwargs), self.loop)

    def shutdown(self):
        print("Shutting down...", flush=True)
        self.loop.call_soon_threadsafe(self.loop.stop)
        #
        # for _ in range(1000):
        #     print(f"Running: {self.loop.is_running()}", flush=True)
        #     if not self.loop.is_running():
        #         break
        #
        #
        # pending_tasks = [t for t in asyncio.all_tasks(self.loop) if not t.done()]
        # if not pending_tasks:
        #     return
        # print(f"Pending tasks left: {len(pending_tasks)}")
        # self.loop.run_until_complete(asyncio.gather(*pending_tasks))
        #
        # print("Closing the loop")
        # self.loop.close()

def main():
    runner = Runner()

    for x in range(3000):
        runner.submit(dummy, x)

    runner.shutdown()
    print(f"Post shutdown; finished: {finished}", flush=True)
    print("MAIN EXIT", flush=True)


if __name__ == "__main__":
    main()