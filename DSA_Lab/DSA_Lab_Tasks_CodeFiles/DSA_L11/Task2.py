def ordered_linear_search(arr, key): 
    for i in range(len(arr)): 
        if arr[i] == key: 
            return i 
        elif arr[i] > key: 
            return -1 
    return -1 

arr = [40, 70, 80, 100, 200] 
key = 80
print("Element found at index:", ordered_linear_search(arr, key))