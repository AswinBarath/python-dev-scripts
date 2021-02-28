# Generators
# Generators creates data one at a time
# range() is an example of a generator

# whereas, iterables creates the entire structure in memory
# and only then we can start using it
# print(list(range(100000))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


my_list = make_list(100)
print(my_list)
