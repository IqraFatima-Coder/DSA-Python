def real_time_insert_sort(arr, new_value):
    i = len(arr) - 1
    arr.append(new_value)
    while i >= 0 and arr[i] > new_value:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = new_value
    return arr

arr = [1, 3, 5, 7]
print("Before:", arr)
real_time_insert_sort(arr, 4)
print("After inserting 4:", arr)
