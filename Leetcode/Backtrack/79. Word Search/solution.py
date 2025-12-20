class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def inBounds(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            return True

        seen = set()
        def dfs(i, j, ind):
            if ind == len(word):
                return True
            elif not inBounds(i, j) or (i, j) in seen or board[i][j] != word[ind]:
                return False
            
            seen.add((i, j))
            l = dfs(i - 1, j, ind + 1)
            r = dfs(i + 1, j, ind + 1)
            u = dfs(i, j - 1, ind + 1)
            d = dfs(i, j + 1, ind + 1)
            seen.remove((i, j))

            return l or r or u or d


        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False