import time
import random

def quick_sort_first(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    more = [x for x in arr[1:] if x > pivot]
    return quick_sort_first(less) + [pivot] + quick_sort_first(more)

def quick_sort_last(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    less = [x for x in arr[:-1] if x <= pivot]
    more = [x for x in arr[:-1] if x > pivot]
    return quick_sort_last(less) + [pivot] + quick_sort_last(more)

arr = [random.randint(0, 10000) for _ in range(1000)]

start = time.time()
quick_sort_first(arr)
print("Quick Sort (First Pivot):", round(time.time() - start, 5), "sec")

start = time.time()
quick_sort_last(arr)
print("Quick Sort (Last Pivot):", round(time.time() - start, 5), "sec")
