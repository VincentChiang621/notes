class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time: O(klogn) | Space: O(n)
        minHeap = []
        for p in points:
            x, y = p
            dist = sqrt((x * x) + (y * y))
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        res = []
        for i in range(k):
            d, x, y = heapq.heappop(minHeap)
            res.append([x,y])

        return res