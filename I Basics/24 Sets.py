# Sets - Unordered collection of unique objects
my_set = {1, 2, 3, 4, 5, 3, 1, 5}
print(my_set)
# No duplicates
my_set.add(100)
my_set.add(40)
print(my_set)

# Task
# my_list = [1,2,3,4,5,3,1,5]
# new_set = set(my_list)
# print(new_set)
# print(1 in new_set)
# print(len(new_set))
# print(list(new_set))
# again_set = new_set.copy()
# print(again_set)
# again_set.clear()
# print(again_set)
# new_set.clear()
# print(new_set)

# Set methods :-
# .difference()
# .discard()
# .difference_update()
# .intersection()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

# my_set = {1,2,3,4,5}
# your_set = {4,5,6,7,8,9,10}
# print('difference method')
# print(my_set.difference(your_set))
# print('discard method')
# print(my_set.discard(5))
# print(my_set)
# print('difference_update method')
# print(my_set.difference_update(your_set))
# print(my_set)
# print('intersection method')
# print(my_set.intersection(your_set))
# print(my_set & your_set)
# print('isdisjoint method')
# print(my_set.isdisjoint(your_set))
# print('union method')
# print(my_set.union(your_set))
# print(my_set | your_set)

# my_set2 = {4,5}
# your_set2 = {4,5,6,7,8,9,10}
# print('issubset method')
# print(my_set2.issubset(your_set2))
# print('issuperset method')
# print(my_set2.issuperset(your_set2))
# print(your_set2.issuperset(my_set2))
