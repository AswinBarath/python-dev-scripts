from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'OMG, it took {t2 - t1} s')
        return result

    return wrapper


def fib(number):
    print('This is generator')
    a = 0
    b = 1
    for num in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


@performance
def fib1():
    for i in fib(100000):
        pass
        # print(i)


@performance
def fib2(number):
    print('This is a list')
    a = 0
    b = 1
    result = []
    for num in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


fib1()
fib2(100000)
