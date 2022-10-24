import random


my_string = input()
reg = 0
while reg != 5:
    for i in my_string:
        print(random.choice(my_string), end='')
    reg += 1
    print(' ', end='')
