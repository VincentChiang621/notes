class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Solution 1: add or not add
        # Time: O(2^n * n) | Space: O(n)
        res = []

        def isPalindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def backtrack(start, end, comb, length):
            if length == len(s):
                res.append(comb.copy())
                return
            elif end > len(s):
                return
            
            if isPalindrome(s[start:end]):
                comb.append(s[start:end])
                backtrack(end, end+1, comb, length + (end-start))
                comb.pop()
            
            backtrack(start, end+1, comb, length)
            

        backtrack(0, 1, [], 0)
        return res

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Solution 2: for loop to immediately prune off non-palindromes 
        # Time: O(2^n * n) | Space: O(n)
        res = []
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(substrings, ind):
            if ind == len(s):
                res.append(substrings.copy())
                return 

            for r in range(ind, len(s)):
                if isPalindrome(ind, r):
                    substrings.append(s[ind:r+1])
                    backtrack(substrings, r+1)
                    substrings.pop()

        backtrack([], 0)

        return res

