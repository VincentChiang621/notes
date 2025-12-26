class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        free = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            degree[c] += 1
            free[p].append(c)

        # initialize queue with no prereq courses

        q = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
                degree[i] = -1

        res = []
        while q:
            courseId = q.popleft()

            res.append(courseId)

            # free up courses
            for crs in free[courseId]:
                degree[crs] -= 1

                # can we take other courses after courseId taken?
                if degree[crs] == 0:
                    degree[crs] = -1
                    q.append(crs)

        return res if len(res) == numCourses else [] 
            
