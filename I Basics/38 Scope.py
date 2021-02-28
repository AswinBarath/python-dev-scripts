# Scope - What variables do I have access to?

# Scope Rules
# 1 - Start with local
# 2 - Parent local?
# 3 - Global
# 4 - built-in python functions

# nonlocal keyword
def outer():
    x = "local"

    def inner():
        # nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)


outer()

# Dependency Injection
# total = 0
# def count(total):
# 	total += 1
# 	return total
# print(count(count(count(total))))

# Not a recommended way to use global keyword
# total = 0
# def count():
# 	global total
# 	total += 1
# 	return total
# count()
# count()
# print(count())

# a = 1
# def parent():
#     # a = 10
#     def confusion():
#         # a = 5
#         return sum  #a
#     return confusion()
# print(parent())
# print(a)

# def some_func():
# 	total = 1000
# print(total)
# Traceback (most recent call last):
#   File "test.py", line 5, in <module>
#     print(total)
# NameError: name 'total' is not defined
