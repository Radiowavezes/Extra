import timeit

def fibonacci_search(lst, target):
    size = len(lst)
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    
    while(f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
        
    while(f2 > 1):
        index = min(start + f0, size - 1)
        if lst[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif lst[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
        
    if (f1) and (lst[size - 1] == target):
        return size - 1
    return None


if __name__=='__main__':
    bin_timer = timeit.timeit(
        stmt="fibonacci_search([-100, -1.5, 2, 3, 4, 6, 31, 101], 6)",
        number=100,
        setup="from __main__ import fibonacci_search"
    )
    print(bin_timer)