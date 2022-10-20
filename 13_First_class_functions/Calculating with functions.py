def enclosing_num(num):
    def enclosed_function(f=None):
        return f(num) if f else num
    return enclosed_function

zero, one, two, three, four, five, six, seven, eight, nine = map(enclosing_num, range(10))

def plus(num): return lambda num2: num2 + num
def minus(num): return lambda num2: num2 - num
def times(num): return lambda num2: num2 * num
def divided_by(num): return lambda num2: int(num2 / num)

print(eight(minus(five())))
