class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree must be fully connected
        if len(edges) != (n - 1):
            return False

        adjMat = {i:[] for i in range(n)}

        for a,b in edges:
            adjMat[a].append(b)
            adjMat[b].append(a)

        def bfs(node):
            q = deque([(node, -1)])
            visited = set()

            while q:
                cur, prev = q.popleft()

                if cur in visited:
                    return False

                visited.add(cur)
                for nei in adjMat[cur]:
                    if nei != prev:
                        q.append((nei, cur))

            return True

        res = 0
        for i in range(n):
            if not bfs(i):
                return False

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            cur = n
            while cur != parent[cur]:
                cur = parent[cur]
            return cur

        def union(a, b):
            parA = find(a)
            parB = find(b)

            if parA == parB:
                return False
            
            if rank[parA] < rank[parB]:
                parent[parA] = parB
                rank[parB] += 1
            else:
                parent[parB] = parA
                rank[parA] += 1

            return True

        for a, b in edges:
            if not union(a, b):
                return False

        return (n - 1) == len(edges)