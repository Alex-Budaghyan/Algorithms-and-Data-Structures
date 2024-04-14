def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


lst = [3, 4, 2, 1, 5, 8, 7, 10, 9]
print(insertion_sort(lst))