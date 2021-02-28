# Key Term - Comprehensions
# list, set, dictionary

# my_list = []
# for char in 'hello':
#     my_list.append(char)
# print(my_list)


# List Comprehension
# my_list = [param for param in iterable]
my_list = [char for char in 'hello']
print(my_list)
my_list1 = [num for num in range(1, 101)]
print(my_list1)
my_list2 = [num*2 for num in range(1, 101)]
print(my_list2)
my_list3 = [num**2 for num in range(1, 101)]
print(my_list3)
my_list1 = [num**2 for num in range(1, 101) if num % 2 == 0]
print(my_list1)
my_list1 = [num**2 for num in range(1, 101) if num % 2 == 0]
print(my_list1)


# Set Comprehension
my_set = {num**2 for num in range(1, 101) if num % 2 == 0}
print(my_set)


# Dictionary Comprehension
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value ** 2 for key, value in simple_dict.items()}
print(my_dict)

my_dict1 = {num: num**2 for num in range(1, 50+1)}
print(my_dict1)
