import heapq

# Step 1: Insertion Sort for sorting small chunks
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Step 2: Jesse Sort implementation
def jesse_sort(data, chunk_size=10):
    # Divide into chunks and sort each chunk
    chunks = [insertion_sort(data[i:i + chunk_size]) for i in range(0, len(data), chunk_size)]
    
    heap = []  # Min-heap to merge sorted chunks
    indices = [0] * len(chunks)  # Keep track of each chunk's current index

    # Initialize heap with first element of each chunk
    for i, chunk in enumerate(chunks):
        if chunk:
            heapq.heappush(heap, (chunk[0], i))

    sorted_result = []

    # Merge process
    while heap:
        val, chunk_index = heapq.heappop(heap)
        sorted_result.append(val)
        indices[chunk_index] += 1
        if indices[chunk_index] < len(chunks[chunk_index]):
            next_val = chunks[chunk_index][indices[chunk_index]]
            heapq.heappush(heap, (next_val, chunk_index))

    return sorted_result

# Sample data (50 elements)
data = [87, 12, 45, 66, 21, 78, 33, 59, 10, 95, 61, 37, 48, 29, 55, 76, 19, 70, 82, 15,
        34, 99, 5, 91, 44, 67, 39, 2, 84, 28, 93, 13, 26, 6, 50, 32, 68, 7, 17, 22,
        53, 75, 4, 97, 30, 40, 80, 25, 92, 63]

# Run Jesse Sort
sorted_data = jesse_sort(data)

# Print results
print("Original Data:")
print(data)
print("\nSorted Data:")
print(sorted_data)
