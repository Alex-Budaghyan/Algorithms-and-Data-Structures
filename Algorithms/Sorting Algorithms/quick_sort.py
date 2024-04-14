import random


# Pivot is the last element in the list
def partition_l(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Pivot is the random element
def partition_r(array, low, high):
    pivot_index = random.randint(low, high)
    array[high], array[pivot_index] = array[pivot_index], array[high]
    i = low - 1
    pivot = array[high]
    for k in range(low, high):
        if array[k] <= pivot:
            i += 1
            array[i], array[k] = array[k], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Pivot is the first element
def partition_f(array, low, high):
    i = low + 1
    pivot = array[low]
    for k in range(low, high):
        if array[k] < pivot:
            array[i], array[k] = array[k], array[i]
            i += 1
            # print(array)
    array[i - 1], array[low] = array[low], array[i - 1]
    return i - 1


def quicksort(arr, low, high):
    if low < high:
        # index = partition_f(arr, low, high)
        # index = partition_l(arr, low, high)
        index = partition_r(arr, low, high)
        quicksort(arr, low, index - 1)
        quicksort(arr, index + 1, high)


lst = [5, 8, 9, 7, 4, 6, 5, 10, 0, 8, 45, 15, 31, 9]
quicksort(lst, 0, len(lst) - 1)
print(lst)

