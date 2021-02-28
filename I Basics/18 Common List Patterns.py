# Tricks in Lists
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print('Length of String')
print(len(basket))
print('Copy of Reverse using List Slicing')
print(basket[::-1])
print(basket)

print('List using range')
print(list(range(101)))

# String method
new_sentence = ' '.join(['hi', 'my', 'name', 'is', 'jojo'])
print(new_sentence)

# Exercise
# fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu', 'Stanley']

friends.sort()
print(friends)

# Solution: (keep in mind there are multiple ways to do this, so your answer may vary.
# As long as it works that's all that matters!)
# friends.extend(new_friend)
# print(sorted(friends))
