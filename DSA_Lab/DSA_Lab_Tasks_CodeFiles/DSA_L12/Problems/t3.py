def selection_sort_swaps(arr):
    swap_count = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swap_count += 1
    print("Sorted:", arr)
    print("Swaps made:", swap_count)

selection_sort_swaps([4, 3, 2, 1])
