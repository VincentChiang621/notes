class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time: O(n * log(max(piles)))
        # Space: O(1)
        l, r = 1, max(piles)

        def isValidK(k: int) -> bool:
            # Time: O(piles.length)
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            return hours <= h

        # Use binary search to find first `k`
        while l < r:
            m = l + ((r - l) // 2)
            valid = isValidK(m)

            if valid:
                r = m
            else:
                l = m + 1

        return l