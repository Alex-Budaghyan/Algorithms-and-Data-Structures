def selection_sort(lst):
    for i in range(len(lst)):
        max_index = 0
        for j in range(len(lst) - i - 1):
            if lst[max_index] < lst[j]:
                max_index = j
        lst[j], lst[max_index] = lst[max_index], lst[j]
    return lst