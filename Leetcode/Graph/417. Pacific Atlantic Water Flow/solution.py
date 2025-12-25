class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Brute force, check every cell
        m, n = len(heights), len(heights[0])

        def inBounds(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            return True
        
        def bfs(cordSet, r, c):
            q = deque([(r, c)])
            
            while q:
                x, y = q.popleft()

                if (x, y) in cordSet:
                    continue

                cordSet.add((x, y))

                if inBounds(x - 1, y) and heights[x][y] <= heights[x-1][y]:
                    q.append((x-1,y))
                if inBounds(x + 1, y) and heights[x][y] <= heights[x+1][y]:
                    q.append((x+1,y))
                if inBounds(x, y - 1) and heights[x][y] <= heights[x][y-1]:
                    q.append((x,y-1))
                if inBounds(x, y + 1) and heights[x][y] <= heights[x][y+1]:
                    q.append((x,y+1))

        pacificSet, atlanticSet = set(), set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    bfs(pacificSet, i, j)

                if j == n-1 or i == m-1:
                    bfs(atlanticSet, i, j)

        # res is intersection of both sets
        res = []
        for c in pacificSet:
            if c in atlanticSet:
                res.append(c)

        return res