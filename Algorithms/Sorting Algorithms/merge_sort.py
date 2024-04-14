def mergesort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid + 1, end)
        merge(arr, start, mid, end)
    return arr


def merge(arr, start, mid, end):
    tmp = arr[:]
    s1 = start
    e1 = mid
    s2 = mid + 1
    e2 = end
    index = start
    while s1 <= e1 and s2 <= e2:
        if tmp[s1] < tmp[s2]:
            arr[index] = tmp[s1]
            s1 += 1
            index += 1
        else:
            arr[index] = tmp[s2]
            s2 += 1
            index += 1
    while s1 <= e1:
        arr[index] = tmp[s1]
        s1 += 1
        index += 1
    while s2 <= e2:
        arr[index] = tmp[s2]
        s2 += 1
        index += 1



arr = [5, 3, 1, 4, 9, 6, 8, 7, 11, -5]
print(mergesort(arr, 0, len(arr) - 1))