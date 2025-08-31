class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        l, r = 0, len(s) - 1

        while l < r:
            # adjust pointers if non-alphanumeric
            if not self.isalphaNum(s[l]):
                l += 1
            elif not self.isalphaNum(s[r]):
                r -= 1
            else:
                # convert to lowercase before comparing
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

        return True

    def isalphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('A') <= ord(c) <= ord('Z') or 
                ord('0') <= ord(c) <= ord('9'))