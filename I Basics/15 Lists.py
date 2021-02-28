# Lists are like arrays
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]
amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])

# List Slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0:2])
print(amazon_cart[0::2])
# We Know Strings are Immutable
# Lists are Mutable
amazon_cart[0] = 'laptop'
print(amazon_cart[0:3])
print(amazon_cart)
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)

# new_cart simply points the same location
new_cart = amazon_cart
new_cart[0] = 'gum'
print(amazon_cart)
