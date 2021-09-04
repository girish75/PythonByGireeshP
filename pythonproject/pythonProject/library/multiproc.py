import time

from multiprocessing import Process


def some_function(time_for_sleep=1):
    print(f'Sleeping {time_for_sleep} second...')
    time.sleep(time_for_sleep)
    print('Done Sleeping...')
