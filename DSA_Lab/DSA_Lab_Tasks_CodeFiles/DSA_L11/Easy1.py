def linear_search_strings(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

# Test
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
key = "Charlie"
print("Element found at index:", linear_search_strings(names, key))
