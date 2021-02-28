# Useful pure functions: map, filter, zip and reduce
from functools import reduce
my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list, 0))
