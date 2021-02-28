# Error Handling
while True:
    try:
        age = int(input("Enter your age:"))
        print(age)
        10/age

    except ValueError:
        print('Enter a valid number for your age!!!')

    except ZeroDivisionError:
        print('Enter age higher than 0')

    else:
        print('Thank you!')
        break
