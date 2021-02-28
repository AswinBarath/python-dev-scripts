# To comment selected lines - command: ctrl + /

user_name = input('Enter your username:')
password = input('Enter your password:')
password_length = len(password)
secret = '*' * password_length

print(f'Your password {secret} is {password_length} letters long')
