def binary_search(lst, target, start, end):
    if start <= end:
        mid = end - (end - start) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return binary_search(lst, target, start, mid - 1)
        else:
            return binary_search(lst, target, mid + 1, end)
    return -1