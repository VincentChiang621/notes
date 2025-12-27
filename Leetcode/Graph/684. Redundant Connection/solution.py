class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}

        def find(e):
            if e not in parent:
                parent[e] = e
            if e not in rank:
                rank[e] = 1
            
            cur = e
            while cur != parent[cur]:
                cur = parent[cur]

            return cur

        def union(a, b):
            parA = find(a)
            parB = find(b)

            if parA == parB:
                return False
            elif rank[parA] < rank[parB]:
                parent[parA] = parent[parB]
                rank[parB] += 1
            else:
                parent[parB] = parent[parA]
                rank[parA] += 1

            return True

        for a,b in edges:
            if not union(a, b):
                return [a, b]

        return [-1,-1]  # never reaches here based on problem statement
            