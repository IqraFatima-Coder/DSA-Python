def binary_search(arr, key): 
    left = 0 
    right = len(arr) - 1 
    while left <= right: 
        mid = (left + right) // 2 
        if arr[mid] == key: 
            return mid 
        elif arr[mid] < key: 
            left = mid + 1 
        else: 
            right = mid - 1 
    return -1
arr = [10, 20, 30, 40, 50]
key = 30
print("Found at Index:",binary_search(arr, key))