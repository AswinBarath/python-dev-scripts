# Ternary Operator

# condition_if_true if condition else condtion_if_false

is_friend = False
can_message = 'message allowed' if is_friend else 'not allowed to message'

print(can_message)

# Short Circuiting -> or operator
is_Friend = False
is_User = True

print(is_Friend or is_User)

if is_Friend or is_User:
    print('best friends forever')
