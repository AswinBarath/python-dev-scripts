# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Snow white', 4)
cat2 = Cat('Timmy', 6)
cat3 = Cat('George O\' Malley', 5)


# 2 Create a function that finds the oldest cat
def oldest_cat():
    if cat1.age > cat2.age and cat1.age > cat3.age:
        return cat1.name, cat1.age
    elif cat2.age > cat3.age:
        return cat2.name, cat2.age
    else:
        return cat3.name, cat3.age


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
who, x = oldest_cat()
print(f'The oldest cat {who} is {x} years old.')
