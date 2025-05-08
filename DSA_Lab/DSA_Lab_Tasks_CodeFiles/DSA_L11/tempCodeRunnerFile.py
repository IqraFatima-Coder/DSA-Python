
def binary_search_recursive(arr, left, right, key): 
    if left > right: 
        return -1 
    mid = (left + right) // 2 
    if arr[mid] == key: 
        return mid 
    elif arr[mid] < key: 
        return binary_search_recursive(arr, mid + 1, right, key) 
    else: 
        return binary_search_recursive(arr, left, mid - 1, key)

arr = [5, 2, 8, 1, 9]  # Unsorted array
key = 8
print("Key found:", binary_search_bool(arr, key))
