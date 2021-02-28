def highest_even(li):
    max = 0
    for a_number in li:
        if a_number > max and a_number % 2 == 0:
            max = a_number
    return max


print(highest_even([11, 2, 3, 4, 8, 10, 16]))


# Another solution
def highest_even2(li):
    evens = []
    for a_number in li:
        if a_number % 2 == 0:
            evens.append(a_number)
    return max(evens)


print(highest_even2([11, 2, 3, 4, 8, 10]))
