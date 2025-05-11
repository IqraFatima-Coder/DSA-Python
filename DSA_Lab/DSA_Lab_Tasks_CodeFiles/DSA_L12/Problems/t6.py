def heapify(arr, n, i):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        print(f"Swap {arr[i]} with {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

arr = [3, 9, 2, 1, 4, 5]
print("Initial array:", arr)
heapify(arr, len(arr), 0)
print("Heapified array:", arr)
