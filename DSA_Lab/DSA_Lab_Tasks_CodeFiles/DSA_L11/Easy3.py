def binary_search_bool(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    return False

# Test
arr = [10, 20, 30, 40, 50]
key = 30
print("Key found:", binary_search_bool(arr, key))
