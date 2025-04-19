import heapq
heap = []
heapq.heappush(heap, 40)
heapq.heappush(heap, 20)
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
print("Min-Heap:", heap)
print("Extracted min:", heapq.heappop(heap))
print("After removal:", heap)