def make_operation(st):
    st2 = []
    for i in st[1:]:
        try:
            m = int(i)
            st2.append(m)
        except:
            continue
    res = int(st2[0])
    if st[0] == '+':
        for i in st2[1:]:
            res += int(i)
    elif st[0] == '-':
        for i in st2[1:]:
            res -= int(i)
    elif st[0] == '*':
        for i in st2[1:]:
            res *= int(i)
    elif st[0] == '/':
        for i in st2[1:]:
            res /= int(i)
    return res

print(make_operation((list((input('input the operator "+-*/" and the string of operands: '))))))
