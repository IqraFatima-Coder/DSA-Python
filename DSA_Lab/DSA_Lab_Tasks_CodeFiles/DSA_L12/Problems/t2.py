def insertion_sort_verbose(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Iteration {i}: {arr}")
    return arr

arr = [5, 3, 4, 1]
insertion_sort_verbose(arr)
