# iterable
# iterate
# generator

# Every generators are iterable
# But the converse is not true


def generator_function(num):
    for i in range(num):
        yield i * 2


# for item in generator_function(1000):
#     print(item)
g = generator_function(100)
print(g)
# O/P: <generator object generator_function at 0x01599418>
print(next(g))
print(next(g))
print(next(g))
# yield pauses a function and comes back to it when next is called

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i*2)
#     return result
#
#
# my_list = make_list(100)
# print(my_list)
