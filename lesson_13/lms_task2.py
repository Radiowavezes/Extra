from operator import add, sub, mul, floordiv

def actions(operat, num2):
    def operation(num):
        return operat(num, num2)
    return operation

summation5 = actions(add, 5)
minus3 = actions(sub, 3)
multiple2 = actions(mul, 2)
dividedby10 = actions(floordiv, 10)

print(summation5(7))
print(minus3(10))
print(multiple2(8))
print(dividedby10(60))
