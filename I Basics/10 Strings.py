# Strings
print(type("Hi hello there"))
print(type('Hey'))
username = 'supercoder'
password = 'supersecret'
long_string = '''
  M
 WOW
|O O|
| | |
|___|
 \_/
'''
print(long_string)
first_name = 'Aswin '
last_name = 'Barath'
full_name = first_name + last_name
print(full_name)

# String Concatenation
print('Hello' + ' Aswin')

# Type conversion
print(type(int(str(100))))
a = str(100)
b = int(a)
c = type(b)
print(c)

# Escape Sequence
# Issue: weather = "It's "kind of" sunny"
weather = "\t It\'s \"kind of\" sunny \n Hope you have a good day"
print(weather)

# Formatted Strings

name = 'John Doe'
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old')

# Python 3 Update:-
print(f'hi {name}. You are {age} years old')

# Python 2
print('hi {}. You are {} years old'.format(name, age))
print('hi {1}. You are {0} years old'.format(name, age))
print('hi {new_name}. You are {new_age} years old'.format(new_name='Sally', new_age='19'))

# String Indexes
selfish = '01234567'
# Index - 01234567
print(selfish[6])

# String Slicing - [start:stop:stepover]
print(selfish[0:2])
print(selfish[0:8])
print(selfish[0:8:2])
print(selfish[1:])
print(selfish[:5])
print(selfish[::1])
print(selfish[-1])
print(selfish[::-1])
print(selfish[::-2])

# Immutability
# We cannot reassign a string
