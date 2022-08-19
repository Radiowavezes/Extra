import random


i = 0
list1 = []
list2 = []
uni_list = []
while i < 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    i += 1
list1.sort() # for checking manually if the code is correct in the end
list2.sort() # 
# print(list1)
# print(list2)
i = 0
while i < 10:
    j = 0
    while j < 10:
        if list1[i] == list2[j]:
            if list1[i] not in uni_list:
                uni_list.append(list1[i])
            j += 1
        else:
            j += 1
    i += 1
print(uni_list)
