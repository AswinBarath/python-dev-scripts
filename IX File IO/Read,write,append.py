# Better way to work with files
# with open('text.txt', mode='r') as my_file:
#     print(my_file.read())

# with open('text.txt', mode='r+') as my_file:
#     print(my_file.readlines())
#     text = my_file.write('hey it\'s me')
#     print(text)

# with open('text.txt', mode='a') as my_file:
#     text = my_file.write(':)\n')
#     print(text)

with open('text.txt', mode='w') as my_file:
    text = my_file.write(':)\n')
    print(text)

with open('sad.txt', mode='w') as my_file:
    text = my_file.write(':((\n')
    print(text)
