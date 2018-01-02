#coding=utf-8


import threading
import itertools
import time
import sys


class Signal:   # 1
    go = True


def spin(msg, signal):  # 2
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):   # 3
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))     # 4
        time.sleep(.1)
        if not signal.go:   # 5
            break
    write(' ' * len(status) + '\x08' * len(status))     # 6


def slow_function():    # 7
    """假装等待I/O一段时间"""
    time.sleep(10)   # 8
    return 42


def supervisor():   # 9
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object: ', spinner)  # 10
    spinner.start()     # 11
    result = slow_function()    # 12
    signal.go = False   # 13
    spinner.join()  # 14
    return result


def main():
    result = supervisor()   # 15
    print('Answer: ', result)


if __name__ == '__main__':
    main()