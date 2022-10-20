my_list =  [*range(1, 101)]
uni_list = []
for i in my_list:
    if i % 7 == 0 and i % 5 != 0:
        uni_list.append(i)
print(uni_list)
