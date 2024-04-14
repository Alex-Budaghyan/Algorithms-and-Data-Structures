def counting_sort(arr):
    max_val, min_val = max(arr), min(arr)
    size = max_val - min_val + 1
    count = [0] * size
    res = [0] * len(arr)
    for num in arr:
        count[num - min_val] += 1
    for i in range(1, size):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        res[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = res[i]

    return arr


lst = [1, 555, 7, 8, 9, 7, 8, 20, 45]
print(counting_sort(lst))
