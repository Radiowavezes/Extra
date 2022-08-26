def strange_math(a, b):
    try:
        return int(a)**2 / int(b)
    except (ValueError, ZeroDivisionError):
        print('Give me an integer and don\'t try to devide by zero!')
        raise


print(strange_math(input('What to devide: '), input('...by: ')))
