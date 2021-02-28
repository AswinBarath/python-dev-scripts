# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False  # changing this will either run or not run the message_friends function.
}

user2 = {
    'name': 'Andrei',
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            result = fn(*args, **kwargs)
            return result
        else:
            print('access denied')
            return
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
message_friends(user2)
