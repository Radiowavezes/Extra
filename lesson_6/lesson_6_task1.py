import random


i = 0
my_list = []
while i != 10:
    my_list.append(random.randint(1, 100))
    i += 1
print(max(my_list))
