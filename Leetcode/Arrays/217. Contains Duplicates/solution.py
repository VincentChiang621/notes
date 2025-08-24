class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(N^2)
        # Space: O(1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(N)
        # Space: O(N)
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
