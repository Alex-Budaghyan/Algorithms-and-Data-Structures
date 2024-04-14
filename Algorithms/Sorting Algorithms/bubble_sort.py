def bubble_sort(arr):
    is_sorted =  True
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = False
        if is_sorted:
            return arr

    return arr


arr1 = [1, 5, 7, 4, 2, 3, 0, -5]
arr2 = [0, 10, 21, 31, 14, -75, -15, -54, 54]
print(bubble_sort(arr1))
print(bubble_sort(arr2))

