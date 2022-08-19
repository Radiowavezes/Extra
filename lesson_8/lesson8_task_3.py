def make_operation(st):
    res = int(st[1])
    if st[0] == '+':
        for i in st[2:]:
            res += int(i)
    elif st[0] == '-':
        for i in st[2:]:
            res -= int(i)
    elif st[0] == '*':
        for i in st[2:]:
            res *= int(i)
    elif st[0] == '/':
        for i in st[2:]:
            res /= int(i)
    return res

print(make_operation((''.join((input('input the operator "+-*/" and the string of operands: '))))))
