class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def inBounds(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            return True

        def bfs(r, c):
            if grid[r][c] == 0:
                return 0

            area = 0
            q = deque([(r, c)])

            while q:
                x, y = q.popleft()

                if (x, y) in visited:
                    continue
                
                visited.add((x, y))
                area += 1

                if inBounds(x + 1, y) and grid[x + 1][y]:
                    q.append((x + 1, y))
                if inBounds(x - 1, y) and grid[x - 1][y]:
                    q.append((x - 1, y))
                if inBounds(x, y + 1) and grid[x][y + 1]:
                    q.append((x, y + 1))
                if inBounds(x, y - 1) and grid[x][y - 1]:
                    q.append((x, y - 1))

            return area

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, bfs(i, j))

        return res
    
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def inBounds(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            return True

        def dfs(r, c):
            if not inBounds(r, c):
                return 0
            elif grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            u = dfs(r - 1, c)
            d = dfs(r + 1, c)
            l = dfs(r, c - 1)
            r = dfs(r, c + 1)
            return u + d + l + r + 1

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res