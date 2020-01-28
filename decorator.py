import time
import os
import psutil

def time_of_function(f):
    def wrapper(*args):
       start = time.time()
       f(*args)
       stop = time.time()
       print('Заняло секунд: {}'.format(stop-start))
    return wrapper

def memory_of_function(f):
    def wrapper(*args):
       proc = psutil.Process(os.getpid())
       a = proc.memory_info().rss / 1000
       f(*args)
       proc = psutil.Process(os.getpid())
       b = proc.memory_info().rss / 1000
       c = b - a
       print('Заняло памяти (Kб):', c)
    return wrapper


@time_of_function
@memory_of_function
def f(x):
    list_mln = []
    for i in range(1, x+1):
        list_mln.append(i)
    return list_mln
f(1000000)

@time_of_function
@memory_of_function
def f_gen(x):
    list_gen = [x for x in range(x+1)]
    return list_gen
f_gen(1000000)


