import random


a = random.choice(range(10))
b = random.choice(range(10))
try:
    c = int(input(f'How much will {a} + {b} be? '))
except ValueError:
    print('Please, enter only numbers')
else:
    if c == a + b:
        print('Yes')
    else:
        print('No')
