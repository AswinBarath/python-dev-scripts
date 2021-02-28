# Useful pure functions: map, filter, zip and reduce
my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


print(map(multiply_by2, my_list))
print(list(map(multiply_by2, [1, 2, 3])))
print(my_list)
