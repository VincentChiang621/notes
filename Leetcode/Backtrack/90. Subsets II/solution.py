class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        def bt(i, arr):
            if i == len(nums):
                res.add(tuple(arr))
                return

            arr.append(nums[i])
            bt(i + 1, arr)

            arr.pop()
            bt(i + 1, arr)

        bt(0, [])

        return list(res)
