# Camel case -> BigObject
# Snake case -> Big_Object


# Default parameters
def say_hello(name='Darth Vader', emoji=';-('):
    print(f'Hellllllooooo {name} {emoji}')


# Positional arguements
say_hello('Aswin', ':)')
# Call, invoke function
say_hello('Kishore', ';)')
say_hello('dirsith', ';-)')
# keyword arguements -> Bad practice
say_hello(emoji=':(', name='Sarvesh')
say_hello()
say_hello('Timmy')


# return keyword
def sum(num1, num2):
    return num1 + num2


print(sum(4, 5))


def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)


total = sum(10, 20)
print(total)
