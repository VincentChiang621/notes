class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openP, closeP, cur):
            if openP == closeP == n:
                res.append(cur)
            elif closeP > openP or openP > n or closeP > n:
                return
            
            dfs(openP + 1, closeP, cur + "(")
            dfs(openP, closeP + 1, cur + ")")

        dfs(0, 0, "")

        return res