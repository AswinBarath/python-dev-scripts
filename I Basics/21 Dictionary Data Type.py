# Dictionary (in other langs, also called hashtables, maps, objects)
dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

# dictionary is an unordered key value pair DataStrucure

print(dictionary['b'])
print(dictionary)

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': True
    }
]

print(my_list[0]['a'][2])

# Dictionary keys - Immutable
dictionary2 = {
    123: [1, 2, 3],
    True: 'hello',
    '123': True
}
# List are mutable so we cannot use it as keys
print(dictionary2[123])
print(dictionary2[True])
print(dictionary2['123'])

# Dictionary methods
user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}
print('Get method')
print(user.get('age', 55))
# Another way to create dictionary
user2 = dict(name='John Doe')
print(user2)
print('keys method')
print('basket' in user.keys())
print('values method')
print('hello' in user.values())
print('Items method')
print(user.items())
# print('clear method')
# print(user.clear())
# print(user)
user3 = user.copy()
print('copy method')
print(user.clear())
print(user3)
print('pop method')
print(user3.pop('age'))
print(user3.popitem())
print(user3)
print('update method')
print(user2.update({'name': 'Aswin'}))
print(user2)
print(user2.update({'names': 'Aswin Barath'}))
print(user2)
