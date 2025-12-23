"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}

        def bfs():
            visited = set()
            q = deque([node])

            while q:
                cur = q.popleft()

                if cur in visited:
                    continue
                elif cur not in oldToNew:
                    oldToNew[cur] = Node(cur.val)
                
                visited.add(cur)

                for nei in cur.neighbors:
                    if nei not in oldToNew:
                        oldToNew[nei] = Node(nei.val)
                        q.append(nei)

                    oldToNew[cur].neighbors.append(oldToNew[nei])
                
        bfs()
        return oldToNew[node]


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        visited = set()

        def dfs(node):
            if not node:
                return None
            elif node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                newNeighbor = dfs(nei)
                oldToNew[node].neighbors.append(newNeighbor)

            return copy
            

        return dfs(node)
