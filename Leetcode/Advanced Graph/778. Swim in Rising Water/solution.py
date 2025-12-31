class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        def inBounds(x, y):
            if x < 0 or x >= n or y < 0 or y >= n:
                return False
            return True

        def bfs():
            res = 0
            minHeap = [(grid[0][0], 0, 0)]  # [[depth_i, x_i, y_i],...]
            visited = set()

            while minHeap:
                depth, x, y = heapq.heappop(minHeap)

                if depth in visited:
                    continue

                res = max(res, depth)
                visited.add(depth)

                # reached bottom right corner
                if x == n-1 and y == n-1:
                    break

                if inBounds(x-1, y):
                    heapq.heappush(minHeap, (grid[x-1][y], x-1, y))
                if inBounds(x+1, y):
                    heapq.heappush(minHeap, (grid[x+1][y], x+1, y))
                if inBounds(x, y-1):
                    heapq.heappush(minHeap, (grid[x][y-1], x, y-1))
                if inBounds(x, y+1):
                    heapq.heappush(minHeap, (grid[x][y+1], x, y+1))

            return res

        return bfs()
                