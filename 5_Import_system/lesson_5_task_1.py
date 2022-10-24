import random


num = random.choice(range(10))
c = 'y'
while c == 'y':
    try:
        user_num = int(input('Please, enter the number from 0 to 10: '))
    except ValueError:
        print('Please, give me the NUMBER')
    if user_num == num:
        print('Mindreader!!!')
        c = input('Try again? y/n ')
    else:
        c = input('Try again? y/n ')
print('Good luck!')
