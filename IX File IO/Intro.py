my_file = open('text.txt')

# print(my_file)
# <_io.TextIOWrapper name='text.txt' mode='r' encoding='cp1252'>

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

print(my_file.readlines())
my_file.close()
