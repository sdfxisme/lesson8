import time

def time_elapsed(f):
    def wrapper(*args):
       start=time.time()
       print(f(*args))
       stop=time.time()
       print("Заняло {} секунд".format(stop-start))
    return wrapper



@time_elapsed
def f(x):
    list_mln = []
    for i in range(1, x+1):
        list_mln.append(i)
    return list_mln
f(1000000)
