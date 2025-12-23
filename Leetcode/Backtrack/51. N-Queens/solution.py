class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        pdiag, ndiag = set(), set()
        board = [['.'] * n for _ in range(n)]

        def dfs(ind):
            if ind == n:
                temp = ["".join(b) for b in board]
                res.append(temp)
                return


            for c in range(n):
                if (c in cols or ind + c in pdiag or ind - c in ndiag):
                    continue

                cols.add(c)
                pdiag.add(ind + c)
                ndiag.add(ind - c)
                board[ind][c] = 'Q'

                dfs(ind + 1)

                cols.remove(c)
                pdiag.remove(ind + c)
                ndiag.remove(ind - c)
                board[ind][c] = '.'
            

        
        dfs(0)

        return res