class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        # Keep only the k largest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        # Add new value to heap
        heapq.heappush(self.min_heap, val)

        # If heap grows beyond size k, remove smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The kth largest element is always at the top of the heap
        return self.min_heap[0]
        
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)