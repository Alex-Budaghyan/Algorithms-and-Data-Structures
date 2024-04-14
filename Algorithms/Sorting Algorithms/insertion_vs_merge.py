import time
import random


def merge_sort(lst, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(lst, start, mid)
        merge_sort(lst, mid + 1, end)
        merge(lst, start, mid, end)
    return lst


def merge(lst, start, mid, end):
    tmp = lst[:]
    s1 = start
    e1 = mid
    s2 = mid + 1
    e2 = end
    index = start
    while s1 <= e1 and s2 <= e2:
        if tmp[s1] < tmp[s2]:
            lst[index] = tmp[s1]
            index += 1
            s1 += 1
        else:
            lst[index] = tmp[s2]
            index += 1
            s2 += 1

    while s1 <= e1:
        lst[index] = tmp[s1]
        index += 1
        s1 += 1

    while s2 <= e2:
        lst[index] = tmp[s2]
        index += 1
        s2 += 1

    return lst

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while lst[j] > key and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


insertion_times = []
merge_times = []
tmp = [random.randint(1, 100) for _ in range(100)]
for i in range(500):
    lst = tmp[:]
    # print(lst)
    start_time = time.time()
    insertion_sort(lst)
    end_time = time.time()
    # print(start_time, end_time)
    insertion_times.append(end_time - start_time)
    start_time = time.time()
    merge_sort(lst, 0, len(lst) - 1)
    end_time = time.time()
    merge_times.append(end_time - start_time)

# print(insertion_times)
# print(merge_times)
res = []
for i in range(len(insertion_times)):
    if insertion_times[i] < merge_times[i]:
        res.append(1)
    elif insertion_times[i] > merge_times[i]:
        res.append(2)
    else:
        res.append(0)

print(f"insertion is best {res.count(1)} times")
print(f"merge is best {res.count(2)} times")
print(f"They are equal {res.count(0)} times")
# print(res)

print(sum(merge_times) - sum(insertion_times))