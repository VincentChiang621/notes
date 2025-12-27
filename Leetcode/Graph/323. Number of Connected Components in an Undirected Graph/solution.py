class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS with visited
        adjMat = {i:[] for i in range(n)}
        for a, b in edges:
            adjMat[a].append(b)
            adjMat[b].append(a)

        visited = set()

        def bfs(node):
            # all nodes in connected component will be added to `visited`
            q = deque([node])
            while q:
                cur = q.popleft()
                if cur in visited:
                    continue

                visited.add(cur)

                for i in adjMat[cur]:
                    q.append(i)
            
        res = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1

        return res


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # UNION FIND
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def union(a, b):
            parA = find(a)
            parB = find(b)

            if parA == parB:
                return
            # connecting two components (decrement n)
            nonlocal res
            res -= 1

            # union by rank
            if rank[parA] < rank[parB]:
                parent[parA] = parB
                rank[parB] += 1
            else:
                parent[parB] = parA
                rank[parA] += 1

        def find(e):
            cur = e
            while cur != parent[cur]:
                cur = parent[cur]
                # optional path compression
                # parent[cur] = parent[parent[cur]]

            return cur

        res = n
        for a, b in edges:
            union(a, b)

        return res
        



