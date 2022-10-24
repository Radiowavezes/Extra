def binary_search(target:int, start:int=0, stop:int=100) -> int:
    middle = (start + stop) // 2
    if middle == target:
        return f'the target was {middle}'
    if middle > target:
        return binary_search(target, start, middle - 1)
    if middle < target:
        return binary_search(target, middle + 1, stop)

print(binary_search(33))
