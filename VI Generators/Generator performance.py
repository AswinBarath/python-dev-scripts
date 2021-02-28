# Decorator
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'OMG, it took {t2 - t1} s')
        return result
    return wrapper


@performance
def long_time1():
    print('1')
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i * 5


long_time1()
long_time2()
# O/P
# 1
# OMG, it took 22.67104196548462 s
# 2
# OMG, it took 198.508713722229 s
