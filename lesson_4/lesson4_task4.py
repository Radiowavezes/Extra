name1 = 'anastasiia'
name_input = str(input("What's your name? "))
name2 = name_input.lower()
seq = 0
if len(name1) != len(name2):
    print('False')
else:
    for i in range(len(name1)):
        if name1[i] != name2[i]:
            seq +=1
    if seq == 0:
        print('True')
    else:
        print('False')
