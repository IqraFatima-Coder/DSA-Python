
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


arr = [1, 8, 0, 2, 9,7]  # Unsorted array
key = 1
print("Key found:", binary_search_bool(arr, key))
