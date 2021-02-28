# Exercise! Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be
# '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

fill = '*'
empty = ' '
for line in picture:
    for pixel in line:
        if pixel:
            print(fill, end="")
        else:
            print(empty, end="")
    print(empty)
