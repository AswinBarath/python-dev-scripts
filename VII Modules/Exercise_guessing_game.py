import sys
import random
beg = int(sys.argv[1])
end = int(sys.argv[2])
number = random.randint(beg, end)
while True:
    try:
        guess = int(input(f'Enter a number b/w {beg} & {end}:'))
        if beg <= guess <= end:
            if number > guess:
                print(f'Oh no, {guess} is lesser than the number')
            elif number < guess:
                print(f'Oh no, {guess} is greater than the number')
            else:
                print(f'Congrats, you won the game!!\nYour guess {guess} is correct')
                break
        else:
            print(f'Hey bozo, I told you to enter a number b/w {beg} & {end}, so')
            continue
    except ValueError:
        print('Hello mister, please enter a number')
        continue
