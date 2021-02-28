# Error Handling
while True:
    try:
        age = int(input("Enter your age:"))
        print(age)
        10/age
    except ValueError:
        print('Enter a valid number for your age!!!')
        continue
    except ZeroDivisionError:
        print('Enter age higher than 0')
        break
    else:
        print('Thank you!')
        break
    finally:
        print('OK, I am done here finally')
    print('Can you hear me?')
