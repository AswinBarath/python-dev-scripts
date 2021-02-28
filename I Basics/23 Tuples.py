# tuple - Immutable
my_tuple = (12, 34, 56, 78, 910)
print(my_tuple[2])
user = {
    (1, 2): [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print('items method prints in tuple')
print(user.items())
print(user[(1, 2)])

# Tuple Slicing
new_tuple = my_tuple[1:4]
print(new_tuple)

x, y, z, *other = my_tuple
print(x)
print(y)
print(z)
print(other)

# Tuple methods
print('count method')
print(my_tuple.count(12))
print('index method')
print(my_tuple.index(56))
print('len method')
print(len(my_tuple))
