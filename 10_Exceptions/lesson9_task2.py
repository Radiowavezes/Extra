def strange_math(a, b):
    try:
        return int(a)**2 / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Give me an integer and don\'t try to devide by zero!'


print(strange_math(input('What to devide: '), input('...by: ')))
