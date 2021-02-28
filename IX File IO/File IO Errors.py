try:
    with open('app//sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File not found error!')
    raise err
except IOError as err:
    print('File I/O error!')
    raise err
