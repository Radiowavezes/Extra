weekdays = {
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
    7 : 'Sunday'
}

reversed_weekdays = {}

for i, j in weekdays.items():
    reversed_weekdays[j] = i
    print(j, ':', i)
