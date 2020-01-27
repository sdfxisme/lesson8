import time

def time_elapsed(f):
    def wrapper(*args):
       start=time.time()
       f(*args)
       stop=time.time()
       print("Заняло {} секунд".format(stop-start))
    return wrapper

@time_elapsed
def f(x):
    list_mln = []
    for i in range(1, x+1):
        list_mln.append(i)
    print(type(list_mln))
    return list_mln
f(1000000)

@time_elapsed
def f_gen(x):
    list_gen = [x for x in range(x+1)]
    print(type(list_gen))
    return list_gen
f_gen(1000000)

@time_elapsed
def f_gen1(x):
    list_gen1 = (x for x in range(x+1))
    print(type(list_gen1), list_gen1)
    return list_gen1
f_gen1(1000000)
