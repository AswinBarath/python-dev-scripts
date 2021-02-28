# OOP
class PlayerCharacter:
    # Class Object attribute
    membership = True

    def __init__(self, name='anonymous', age=0):  # constructor
        if age > 18:
            self.name = name        # attributes
            self.age = age

    def shout(self):                  # Method
        print(f'run {self.name} run you\'re {self.age}')
        return 'done'

    def run(self):                  # Method
        print(f'run {self.name}')
        return 'done'


player1 = PlayerCharacter('Forrest', 44)
player2 = PlayerCharacter('Tom', 21)
print(player1)
print(player2)
print(player1.run)
print(player1.run())
print(player1.shout())
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)
