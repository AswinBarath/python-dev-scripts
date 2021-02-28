print(4 > 5)
print(4 < 5)
print(4 == 5)
print('a' > 'A')

# Python function to print the UNICODE value of characters
print(ord('A'))
print(ord('a'))

a = [1, 2, 3]
b = a
print(a is b, '\n')

for i in 'Zero To Mastery':
    print(i, end='\t')
print('\n')
thisset = {"apple", "banana", "cherry", "apple"}

thisset.update(["orange", "mango", "grapes", "apple"])

print(thisset)

import re
s = 'Hi I am Aswin BArath with USN 18btrse 031'
print(re.findall('[a-z0-9]+', s))

print(range(10))
print(list(range(10)))
print(list(range(100, 0, -3)))
for _ in range(10, 0, -2):
    print(_)
    print('check check')
