# Error Handling
# Good practice is to catch specific errors to be more descriptive
def sum_of_2(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('Something\'s wrong here! hmmm! Because:', err)
        print(f'The error occurred - {err}')


print(sum_of_2('234', 3.3))
