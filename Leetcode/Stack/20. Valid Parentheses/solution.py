class Solution:
    def isValid(self, s:str) -> bool:
        # Time: O(n) | Space: O(n)
        parenMap = { ')': '(', '}': '{', ']': '[' }
        paren = []

        for c in s:
            # closing bracket 
            if c in parenMap:
                if not paren or parenMap[c] != paren[-1]:
                    return False
                paren.pop()
            else:
                paren.append(c)

        return len(paren) == 0