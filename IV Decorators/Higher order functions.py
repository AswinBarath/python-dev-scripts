# Higher Order Function HOC
# It's either a Function which accepts a function as a parameter
# or returns a function
def greet(func):
    func()
# Other Examples: map(), filter(), reduce(), zip() --> accepts a func


def greet2():
    def func():
        return 5
    return func
