class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(N) | Space: O(N)

        # O(N = len(tasks))
        hMap = {}
        for t in tasks:
            hMap[t] = hMap.get(t, 0) + 1

        # O(N = len(tasks))
        maxHeap = []
        for key, val in hMap.items():
            maxHeap.append(-val)

        # O(N = len(tasks))
        heapq.heapify(maxHeap)

        mostFreq = -1 * heapq.heappop(maxHeap)
        blocks = n + 1
        numBlocks = mostFreq - 1
        add = 1

        # O(26 * log(N))
        while maxHeap and n > 0:
            nextFreq = -1 * heapq.heappop(maxHeap)
            if nextFreq == mostFreq:
                add += 1
            else:
                break
            n -= 1

        return max(blocks * numBlocks + add, len(tasks))


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(N * log26) | Space: O(N)

        # O(N = len(tasks))
        freq = [0] * 26  # ind0 = 'A', 1 = 'B', to frequency
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        # O(N = len(tasks))
        maxHeap = [-n for n in freq if n != 0]
        heapq.heapify(maxHeap)

        queue = deque()
        time = 0

        # O(N * log26)
        while queue or maxHeap:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    queue.append([cnt, time + n])

            if queue:
                if queue[0][1] <= time:
                    cnt, t = queue.popleft()
                    heapq.heappush(maxHeap, cnt)

        return time