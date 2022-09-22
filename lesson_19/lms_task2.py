def in_range(start, stop, step=1):
    current = start
    while current < stop:
        yield current
        current += step


print(*in_range(2, 10, 3))
