class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return False
            elif (r < 0 or r >= m or c < 0 or c >= n
                  or grid[r][c] == '0'):
                return False

            visited.add((r, c))

            # add up, down, left, right
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
            return True
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j):
                    res += 1

        return res
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(r, c):
            if (r, c) in visited or grid[r][c] == '0':
                return False
            
            q = deque([(r, c)])

            while q:
                x, y = q.popleft()

                if (x < 0 or x >= m or y < 0 or y >= n 
                    or (x, y) in visited or grid[x][y] == '0'):
                    continue 

                visited.add((x, y))
                
                q.append((x + 1, y))
                q.append((x - 1, y))
                q.append((x, y + 1))
                q.append((x, y - 1))
            
            return True
        
        for i in range(m):
            for j in range(n):
                if bfs(i, j):
                    res += 1

        return res