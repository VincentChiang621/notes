class Solution:
    def simplifyPath(self, path: str) -> str:
        # Time: O(n)
        # Space: O(n)
        dirs = path.split('/')
        res = []

        for d in dirs:
            if not d or d == '.':
                continue
            elif d == '..':
                res.pop() if res else None
            else:
                res.append(d)

        return '/' + '/'.join(res)
        