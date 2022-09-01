def persist(n, count=0):
    res = 1
    if len(str(n)) == 1:
        return count
    for i in str(n):
        res *= int(i)
    return persist(res, count + 1)

print(persist(39))