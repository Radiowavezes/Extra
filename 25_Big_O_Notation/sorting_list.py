def sort_list(any_list_to_sort: list[int]) -> list[int]:
    '''
    Function sorts the lists of integers
    '''
    temp: list[int] = any_list_to_sort[:]
    result_list = []
    while len(temp) > 0:
        item = min(temp)
        result_list.append(item)
        temp.remove(item)
    return result_list

list_to_sort = [5, 9, 3, 4, 2, 8, 1]
list_to_sort2 = ['f', 's', 'g', 'r', 'h', 'j', 'd']
print(sort_list(list_to_sort))
print(sort_list(list_to_sort2))
