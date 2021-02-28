import random

# help(random)
# print(random)
# print(dir(random))

print(random.random())
print(random.randint(1, 10))
print(random.choice([77, 22, 99, 66, 55]))
my_list = [9, 7, 4, 2, 1]
random.shuffle(my_list)
print(my_list)
