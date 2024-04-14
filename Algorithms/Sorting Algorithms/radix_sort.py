def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(size - 1, -1, -1):
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
    for i in range(0, size):
        array[i] = output[i]


def radix_sort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
    return array


lst = [921, 428, 576, 1024, 46, 5]
print(radix_sort(lst))
