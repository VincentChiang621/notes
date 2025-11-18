class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(sub):
            if len(sub) == len(nums):
                res.append(sub.copy())

            for n in nums:
                if n not in sub:
                    sub.append(n)
                    dfs(sub)
                    sub.pop()

        dfs([])
        return res