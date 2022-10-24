my_string = str(input())
if len(my_string) >= 2:
    print(my_string[0:2] + my_string[-2:len(my_string)])
else:
    print()
