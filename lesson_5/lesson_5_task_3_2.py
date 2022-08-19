import random


my_string = input()
obg = ''
reg = 0
my_list = []
while reg < 5:
    for i in my_string:
        obg += (random.choice(my_string))
    my_list.append(obg)
    obg = ''
    reg += 1
print(my_list)
