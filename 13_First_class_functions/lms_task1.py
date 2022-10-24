def transposed(li):
        res = []
        for i in range(len(li[0])):
            row = []
            for j in li:
                row.append(j[i])
            res.append(row)
        return res

print(transposed.__code__.co_nlocals)
