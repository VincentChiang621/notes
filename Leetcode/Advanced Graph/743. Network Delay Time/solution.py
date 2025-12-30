class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMat = {i:[] for i in range(1, n+1)}

        for src, tar, wei in times:
            adjMat[src].append([tar, wei])

        minHeap = [[0, k]]
        shortest = {i:-1 for i in range(1, n+1)}
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if shortest[n1] >= 0:
                continue
            
            shortest[n1] = w1

            for n2, w2 in adjMat[n1]:
                if shortest[n2] < 0:
                    heapq.heappush(minHeap, [w1+w2, n2])

        if -1 not in shortest.values():
            return max(shortest.values())
        return -1
