#coding=utf-8


import time
import asyncio


async def do_some_work(x):
    print('Waiting {}'.format(x))
    return 'Done after {}s'.format(x)

start = time.time()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)
loop.run_until_complete(task)
print('Task ret: {}'.format(task.result()))
print('TIME: {}'.format(time.time() - start))

