class Solution:
    def reorganizeString(self, s: str) -> str:
        # Time: O(len(s)) | Space: O(26)
        # count frequency of chars in s
        counter = {}    # stores char->freq
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        # initialize maxHeap
        maxHeap = [[-val, key] for key, val in counter.items()]
        heapq.heapify(maxHeap)

        res = ""
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            if len(res) > 0 and res[-1] == char:    # Two Adjacent Chars
                # no possible rearrangement
                if len(maxHeap) == 0:
                    return ""
                freq2, char2 = heapq.heappop(maxHeap)
                res += char2
                if freq2 + 1 < 0:
                    heapq.heappush(maxHeap, [freq2 + 1, char2])
                
                # add the first char back
                heapq.heappush(maxHeap, [freq, char])
            else:   # Normal Case
                res += char
                if freq + 1 < 0:
                    heapq.heappush(maxHeap, [freq + 1, char])

        return res