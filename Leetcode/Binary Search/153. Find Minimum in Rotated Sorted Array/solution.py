class Solution:
    def findMin(self, nums:List[int]) -> int:
        # Time: O(log(n))
        # Space: O(1)
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            # left ascending
            if nums[l] <= nums[mid]:
                res = min(res, nums[l])
                l = mid + 1
            else:
                res = min(nums[mid], res)
                r = mid - 1

        return res