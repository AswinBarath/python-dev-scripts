for i, c in enumerate('Helllooo'):
    print(i, c)
for i, num in enumerate(list(range(100))):
    print(i, num)
    if num == 50:
        print(f'index of 50 is: {i}')

j = 0
while j < 50:
    print(j, end=" ")
    j += 1
else:
    print("OVER!!!")

# Why else? Here's why!
k = 0
while k < 50:
    print(k, end=" ")
    k += 1
    break
else:
    print("OVER!!!")

while True:
    response = input("Say something: ")
    if response == 'bye':
        break
