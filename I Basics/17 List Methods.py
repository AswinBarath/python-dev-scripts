# Built in function
basket = [1, 2, 3, 4, 5]
print(len(basket))

# List Methods
# adding
basket.append(100)
new_list = basket
print('append method')
print(basket)
print(new_list)

basket.insert(4, 100)
print('Insert method')
print(basket)

basket.extend([101])
print('Extend method')
print(basket)

# removing
basket.pop()
basket.pop(4)
popped = basket.pop(5)
print('Pop methods')
print(basket)
print(popped)

basket.remove(2)
print('Remove method')
print(basket)

basket.clear()
print('Clear method')
print(basket)

trolley = ['c', 'a', 'b', 'c', 'd', 'e', 'c']
# Index ->  0   1   2   3   4
print('Index method')
print(trolley.index('d', 0, len(trolley)))
print('d' in trolley)
print('x' in trolley)
print('w' in 'I\'m Aswin')

print(trolley.count('c'))

# Exercise
# using this list,
basket2 = ["Banana", "Apples", "Oranges", "Blueberries"]

print(basket2)
# 1. Remove the Banana from the list
basket2.remove("Banana")
print(basket2)
# 2. Remove "Blueberries" from the list.
basket2.pop()
print(basket2)
# 3. Put "Kiwi" at the end of the list.
basket2.append('Kiwi')
print(basket2)
# 4. Add "Apples" at the beginning of the list
basket2.insert(0, 'Apples')
print(basket2)
# 5. Count how many apples in the basket
basket2.count('Apples')
print(basket2)
# 6. empty the basket
basket2.clear()
print(basket2)

basket3 = ['e', 'd', 'c', 'x', 'd', 'b', 'a']
basket3.sort()
print('Sort method')
print(basket3)
# Built in function
print(sorted(basket3))
print(basket3)
new_basket = basket.copy()
new_basket.sort()
print(new_basket)
print(basket3)

print(basket3)
print('Reverse method')
basket3.reverse()
print(basket3)
