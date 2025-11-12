class MedianFinder:
    def __init__(self):
        self.firstHalf = []     # maxHeap tracks smaller portion
        self.secHalf = []       # minHeap tracks larger portion

    def addNum(self, num: int) -> None:
        # O(logn)
        heapq.heappush(self.secHalf, num)

        # maintain correctness of two Heaps
        if self.firstHalf and abs(self.firstHalf[0]) > self.secHalf[0]:
            n = heapq.heappop(self.secHalf)
            heapq.heappush(self.firstHalf, -n)

        # maintain len(firstHalf) <= len(secHalf)
        if len(self.secHalf) - len(self.firstHalf) > 1:
            n = heapq.heappop(self.secHalf)
            heapq.heappush(self.firstHalf, -n)
        elif len(self.firstHalf) > len(self.secHalf):
            n = heapq.heappop(self.firstHalf)
            heapq.heappush(self.secHalf, -n)

    def findMedian(self) -> float:
        # O(1)
        if len(self.firstHalf) == len(self.secHalf):
            return ((-self.firstHalf[0]) + self.secHalf[0]) / 2
        
        return self.secHalf[0]