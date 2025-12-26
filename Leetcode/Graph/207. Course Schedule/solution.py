class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS for cycle detection
        # map courses with prerequisites
        adjMat = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            adjMat[c].append(p)
        

        visited = set()
        def dfs(cNum):
            if adjMat[cNum] == []:
                return True
            elif cNum in visited:
                return False

            visited.add(cNum)

            for p in adjMat[cNum][::-1]:
                if dfs(p):
                    adjMat[cNum].pop()
                else:
                    return False

            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
    
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological Sort: Kahn's Algorithm
        # count how many incoming prerequisites into course c
        degree = [0] * numCourses
        free = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            degree[c] += 1
            free[p].append(c)

        # initialize queue with courses that have no prerequisites
        q = deque()
        seen = set()
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
                seen.add(i)

        top = []
        while q:
            courseId = q.popleft()

            top.append(courseId)
            # take this course, free up courses
            for c in free[courseId]:
                degree[c] -= 1

            for i in range(len(degree)):
                if i not in seen and degree[i] == 0:
                    seen.add(i)
                    q.append(i)

        if len(top) == numCourses:
            return True
        return False
