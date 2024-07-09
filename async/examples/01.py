"""
Normal Python Version
"""

# import time
#
#
# def do_work(s: str, delay_s: float = 1.0):
#     print(f"{s} started")
#     time.sleep(delay_s)
#     print(f"{s} done")
#
#
# def main():
#     start = time.perf_counter()
#     todo = ["get package", "laundry", "bake cake"]
#
#     for item in todo:
#         do_work(item)
#
#     end = time.perf_counter()
#     print(f"it took: {end - start:.2f}s")
#
#
# if __name__ == "__main__":
#     main()
"""
USAGE:
╰─$ python3 01.py
get package started
get package done
laundry started
laundry done
bake cake started
bake cake done
it took: 3.01s

A lot of time is wasted in waiting,
instead of just start everything, then wait at the same time
"""

import time
import asyncio


async def do_work(s: str, delay_s: float = 1.0):
    print(f"{s} started")
    await asyncio.sleep(delay_s)
    print(f"{s} done")


async def main():
    start = time.perf_counter()
    todo = ["get package", "laundry", "bake cake"]
    """
    for item in todo:
        await do_work(item)

    The previous loop will not work now
    """
    # 1st version of async gather
    # tasks = [asyncio.create_task(do_work(item)) for item in todo]
    # done, pending = await asyncio.wait(tasks)

    # 2nd version of async gather
    # tasks = [do_work(item) for item in todo]
    # results = await asyncio.gather(*tasks, return_exceptions=True)

    # 3rd version of async gather
    async with asyncio.TaskGroup() as tg:  # python 3.11 +
        tasks = [tg.create_task(do_work(item)) for item in todo]

    end = time.perf_counter()
    print(f"it took: {end - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())

"""
coroutine_function() -> coroutine 
use asyncio.run() to start the coroutine

a coroutine is a light weight task


using any of the 3 version of async gathering of tasks can do the job
with the same speed performance,


╰─$ python3 async/examples/01.py
get package started
laundry started
bake cake started
get package done
laundry done
bake cake done
it took: 1.00s
"""
