# Useful pure functions: map, filter, zip and reduce
my_list = [1, 2, 3]


def only_even(item):
    return item % 2 == 0


print(filter(only_even, my_list))
print(list(filter(only_even, my_list)))
print(my_list)
