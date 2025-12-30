class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's Algorithm (Minimum Spanning Tree)
        # Greedy approach by keep choosing the minimum costs edges (choose n-1 edges)
        # use union find to efficiently find parents (cycle detection)

        # connect the whole graph (complete graph)
        minHeap = []
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dist = abs(x1-x2) + abs(y1-y2)
                minHeap.append([dist, points[i], points[j]])

        heapq.heapify(minHeap)

        parents = {}
        rank = {}
        def find(a):
            a = tuple(a)
            if a not in parents:
                parents[a] = a
            if a not in rank:
                rank[a] = 1

            cur = parents[a]
            while cur != parents[cur]:
                cur = parents[cur]
            return cur

        def union(a, b):
            # returns false if we will create a cycle if we union a,b
            # else unions(a, b) and returns True
            a = tuple(a)
            b = tuple(b)
            parA = find(a)
            parB = find(b)

            if parA == parB:
                return False
            elif rank[parA] < rank[parB]:
                rank[parB] += 1
                parents[parA] = parB
            else:
                rank[parA] += 1
                parents[parB] = parA

            return True
            
        res, chosen = 0, 0        
        while minHeap:
            dist, v1, v2 = heapq.heappop(minHeap)
            
            isSuccess = union(v1, v2)
            # if picking this edge creates cycle
            if not isSuccess:
                continue
            else:
                res += dist
                chosen += 1

                if chosen == len(points) - 1:
                    break

        return res
        
