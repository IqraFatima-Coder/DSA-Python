import time
import random

arr = list(range(900)) + random.sample(range(900, 1000), 100)
random.shuffle(arr)

def insertion_sort_trace(arr):
    start = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return time.time() - start

print("Insertion Sort Time (90% sorted):", insertion_sort_trace(arr), "sec")
