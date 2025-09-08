class Solution:
    def characterReplacement(self, s:str, k:int) -> int:
        # Time O(N) | Space: O(N)
        charMap = defaultdict(int)
        l, res = 0, 0
        # max_f = 0

        for r in range(len(s)):
            charMap[s[r]] += 1
            # max_f = max(max_f, charMap[s[r]])
            max_f = max(charMap.values())
            while k < (r - l + 1) - max_f:
                charMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res