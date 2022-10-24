def with_index(iterable, start=0):
    current = start
    for item in iterable:
        yield current, item
        current += 1

my_list = ['a', 'b', 'C', 'De', 'x', 'P']
print(*with_index(my_list, 2))
