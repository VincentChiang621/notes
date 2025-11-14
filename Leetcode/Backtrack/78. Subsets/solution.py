class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n*2^n) | Space: O(n)
        res = []

        def dfs(i, sub):
            if i == len(nums):
                res.append(sub.copy())
                return

            dfs(i + 1, sub)

            sub.append(nums[i])
            dfs(i + 1, sub)
            sub.pop()


        dfs(0, [])
        return res