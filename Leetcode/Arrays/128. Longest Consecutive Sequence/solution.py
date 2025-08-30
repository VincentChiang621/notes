class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        numset = set(nums)
        longest = 0

        for n in numset:
            # only count if n is starting sequence
            if n - 1 not in numset:
                length = 0
                while n + length in numset:
                    length += 1
                longest = max(longest, length)

        return longest