# Functions in Python act like first class citizens
# That is it can be passed as variable in Python
def hello():
    print('Helllllooooo')


# greet = hello()
# print(greet)
greet = hello
del hello
print(greet)
print(greet())


# Functions can be passed inside of arguments
def helllo(func):
    func()


def greeet():
    print('still here! hehehe!')


a = helllo(greeet)
print(a)
