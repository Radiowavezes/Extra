def bubble_sort(array):
    div = 0
    for i in range(len(array) - 1, 1, -1):
        for j in range(div, i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
        for j in range(i - 1, div):
            if array[j] < array[j - 1]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
        div += 1
    return array

array = [9, 1, 15, 28, 6, 35, 12, 62, 43, 8, 51]
print(bubble_sort(array))