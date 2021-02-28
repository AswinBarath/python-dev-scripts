# Pure Functions has two rules
# 1. Given the same input, it will always return the same output
# 2. A function should not produce any side effects
#   Note: Side effects are things that a function does that affect the outside world
#         For Example: Printing, Accessing variable outside scope

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3]))
