class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time O(n^2) | Space: O(n)
        if not s:
            return 0

        longest = 1

        for i in range(len(s)):
            dup = set(s[i])
            for j in range(i + 1, len(s)):
                if s[j] in dup:
                    break

                dup.add(s[j])

            longest = max(longest, len(dup))

        return longest

    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time O(n) | Space: O(n)
        res, l = 0, 0
        dupMap = set()

        for r in range(len(s)):
            while s[r] in dupMap:
                print(s[l])
                dupMap.remove(s[l])
                l += 1

            dupMap.add(s[r])
                
            res = max(res, len(dupMap))

        return res

