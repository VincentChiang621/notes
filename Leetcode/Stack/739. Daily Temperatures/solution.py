class Solution:
    def dailyTemperatures(self, temperatures:List[int]) -> List[int]:
        # Time: O(N)
        # Space: O(N)
        N = len(temperatures)
        res = [0] * N
        stack = []  # pair [temp, ind]

        for i, n in enumerate(temperatures):

            while stack:
                topV, topI = stack[-1]
                if topV < n:
                    res[topI] = i - topI
                    stack.pop()
                else:
                    break

            stack.append([n, i])

        return res