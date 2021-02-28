class PlayerCharacter:
    # Class Object Attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age >= 18:
            self.name = name
            self.age = age

    def shout(self, hello):
        print(f'Hey there, {hello}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Tom', 21)
player2 = PlayerCharacter('Alice', 18)
player1.shout('Hellllooo')
player2.shout('What\'s uppp')
player3 = PlayerCharacter.adding_things(10, 20)
print(player3.name, player3.age)
print(player3.adding_things2(2, 4))
