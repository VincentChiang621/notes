class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Time: O(N = a+b+c) | Space: O(1)
        maxHeap = []

        for n in [[-a, 'a'], [-b, 'b'], [-c, 'c']]:
            if n[0] != 0:
                maxHeap.append(n)

        heapq.heapify(maxHeap)

        res = ''
        while maxHeap:
            topF, topL = maxHeap[0]
            if len(res) >= 2 and (res[-2] == res[-1] == topL):
                heapq.heappop(maxHeap)

                # second most freq
                if maxHeap:
                    secF, secL = heapq.heappop(maxHeap)
                    res += secL
                    if secF + 1 < 0:
                        heapq.heappush(maxHeap, [secF + 1, secL])
                else:
                    break
                # add the topfreq back
                heapq.heappush(maxHeap, [topF, topL])
            else:
                freq, letter = heapq.heappop(maxHeap)
                res += letter
                if freq + 1 < 0:
                    heapq.heappush(maxHeap, [freq + 1, letter])

        return res

