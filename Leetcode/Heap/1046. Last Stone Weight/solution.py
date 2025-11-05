class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time: O(nlogn) | Space: O(n)
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = heapq.heappop(maxHeap)
            x = heapq.heappop(maxHeap)

            if x != y:
                newStone = y - x
                heapq.heappush(maxHeap, newStone)

        return -maxHeap[0] if maxHeap else 0