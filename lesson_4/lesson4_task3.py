a = int(input('Enter "a" from 1 to 99 '))
b = int(input('Enter "b" from 1 to 99 '))
try:
    c = int(input('a x b = '))
except ValueError:
		print('Please, enter only numbers')
else:
    if c == a * b:
        print('Yes')
    else:
        print('No')
