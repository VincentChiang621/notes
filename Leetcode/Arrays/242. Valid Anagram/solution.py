class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(Slog(S))
        # Space: O(max(S))
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(len(s))
        # Space: O(1) -> bounded by 26 chars
        if len(s) != len(t):
            return False

        hashS = {}
        # fill up hashS
        for c in s:
            hashS[c] = hashS.get(c, 0) + 1

        # check we have other extra chars
        for c in t:
            if c not in hashS:
                return False
            
            hashS[c] -= 1

            if hashS[c] < 0:
                return False

        return True