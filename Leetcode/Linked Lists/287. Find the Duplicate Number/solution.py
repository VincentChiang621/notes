class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Time: O(n) | Space: O(1)
        slow, fast = 0, 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow