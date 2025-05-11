import time
import random

data = [random.randint(0, 1000) for _ in range(500)]

def timed_sort(sort_func, arr):
    copy = arr[:]
    start = time.time()
    sort_func(copy)
    end = time.time()
    return end - start

def bubble(arr):  # basic bubble
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print("Bubble Sort Time:", timed_sort(bubble, data), "seconds")
print("Selection Sort Time:", timed_sort(selection, data), "seconds")
print("Insertion Sort Time:", timed_sort(insertion, data), "seconds")
