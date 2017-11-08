#coding=utf-8

# import asyncio
# import time
#
#
# now = lambda: time.time()
#
# async def do_some_work(x):  # async定义协程函数,必须加入到事件循环才能执行
#     print('Waiting: ', x)
#
#
# start = now()
#
# coroutine = do_some_work(2)
#
# loop = asyncio.get_event_loop() # 创建一个循环
# loop.run_until_complete(coroutine)  # 协程加入循环
# print('Time: ', now() - start)

# import asyncio
# import time
#
# now = lambda: time.time()
#
# async def do_some_work(x):
#     print('Waiting: ', x)
#
# start = now()
#
# coroutine = do_some_work(2)
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print(task)
# loop.run_until_complete(task)
# print(task)
# print('TIME: ', now() - start)

import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)


def callback(future):
    print('Callback: ', future.result())


start = now()
coroutine = do_some_work(2)