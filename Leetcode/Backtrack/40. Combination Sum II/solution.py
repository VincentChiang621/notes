class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(ind, curSum, comb):
            if curSum == target:
                res.append(comb.copy())
                return
            elif ind >= len(candidates) or curSum > target:
                return

            # use candidate[i]
            comb.append(candidates[ind])
            backtrack(ind + 1, curSum + candidates[ind], comb)
            comb.pop()

            # shift repeated chars
            while (ind + 1) < len(candidates) and candidates[ind] == candidates[ind + 1]:
                ind += 1

            # skip candidate[i]
            backtrack(ind + 1, curSum, comb)

        
        backtrack(0, 0, [])
        return res