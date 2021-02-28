# Lambda expression
from functools import reduce
my_list = [1, 2, 3]
print(my_list)

# def multiply_by2(item):
#     return item * 2
# print(list(map(multiply_by2, my_list)))

print(list(map(lambda item: item * 2, my_list)))


# def only_even(item):
#     return item % 2 == 0
# print(list(filter(only_even, my_list)))

print(list(filter(lambda item: item % 2 == 0, my_list)))


# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item
# print(reduce(accumulator, my_list, 0))

print(reduce(lambda acc, item: acc + item, my_list))
