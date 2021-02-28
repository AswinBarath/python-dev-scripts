# clean code

def is_even(num):
    '''
    Returns True if the param num is an even number
    '''
    return num % 2 == 0


# (3)We don't need conditionals too as we are returning boolean values
# if num % 2 == 0:
# return True
# return False

# (2)We don't need else as if num is even it'll exit the function
# else:
# return False

# (1)We don't need elif as num is not even means it's odd
# elif num % 2 != 0:
# return False

print(is_even.__doc__)
print(is_even(52))
print(is_even(5))
