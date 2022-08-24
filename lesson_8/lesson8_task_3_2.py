def math_do(a, *args):
    res = 0
    j = 1
    if a == '+':
        for i in args:
            res += int(i)
    else:
        res = args[0]
        while j < len(args):
            res -= args[j]
            j += 1
    return res

print(math_do(input(), 1, 2, 3))
