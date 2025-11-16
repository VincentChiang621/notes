class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(i, sub, curSum):
            if curSum == target:
                res.append(sub.copy())
                return
            elif curSum > target:
                return
            
            for i in range(i, len(candidates)):
                if (curSum + candidates[i]) > target:
                    break
                sub.append(candidates[i])
                dfs(i, sub, curSum + candidates[i])
                sub.pop()

        dfs(0, [], 0)
        return res
