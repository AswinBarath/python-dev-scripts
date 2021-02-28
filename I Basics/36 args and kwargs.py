# Special characters
#  *args and **kwargs

def super_func(name, *args, i='hi', **kwargs):
    total = 0
    print(*args)
    print(args)
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func('Andy', 1, 2, 3, 4, 5, num1=5, num2=10))

# Rule of order:
# params, *args, default params, **kwargs
