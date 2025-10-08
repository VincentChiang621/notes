class Solution:
    def search(self, nums:List[int], target:int) -> int:
        # Time: O(logn) | Space: O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r - l) // 2 + l
            if nums[m] == target:
                return m
            # LEFT Sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # RIGHT Sorted
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1                

        return -1