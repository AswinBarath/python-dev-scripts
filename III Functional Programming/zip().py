# Useful pure functions: map, filter, zip and reduce
my_list = [1, 2, 3]
your_list = (22, 44, 66)
their_list = {100, 200, 300}


def only_even(item):
    return item % 2 == 0


print(list(zip(my_list, your_list, their_list)))
print(my_list)
