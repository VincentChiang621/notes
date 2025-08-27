class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(1) output doesnt count as extra space
        res = [1] * len(nums)

        # fill res for prefix product
        mult = nums[0]
        for i in range(1, len(nums)):
            res[i] *= mult
            mult *= nums[i]

        # fill res for postfix product
        mult = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= mult
            mult *= nums[i]

        return res