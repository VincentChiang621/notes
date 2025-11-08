class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(klogn + n) | Space: O(n)
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)


        res = nums[0]
        for i in range(k):
            res = -heapq.heappop(maxHeap)


        return res
