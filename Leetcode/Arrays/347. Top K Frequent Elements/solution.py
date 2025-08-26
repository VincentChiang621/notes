class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(nlogk)
        # Space O(n)        
        # Count frequencies
        freqCount = defaultdict(int)
        for n in nums:
            freqCount[n] += 1

        # Use maxHeap to track frequency
        freq = []
        for key, val in freqCount.items():
            freq.append((-val, key))    # sort by tuples (freq, element)
        heapq.heapify(freq)
        
        # Extract Top k
        res = []
        for _ in range(k):
            new = heapq.heappop(freq)
            res.append(new[1])

        return res

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(nlogk)
        # Space O(n) 
        # Bucket Sort: frequencies -> values
        # [1,2,3,...,len(nums)] frequencies

        # Count element frequency
        freqCount = defaultdict(int)    # element -> freq
        for n in nums:
            freqCount[n] += 1

        # Fill our bucket
        freq = [[] for i in range(len(nums))]
        for key, val in freqCount.items():
            freq[val - 1].append(key)

        # Extract k-frequent
        res = []
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(freq[i])):
                res.append(freq[i][j])
                if len(res) == k:
                    return res

        return ['error']   # placeholder
