class Solution:
    def twoSum(self, numbers:List[int], target:int) -> List[int]:
        # Time: O(n)
        # Space: O(1)
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                return [l + 1, r + 1]
            elif curSum < target:
                l += 1
            else:
                r -= 1

        # placeholder (since we are guarenteed one solution)
        return None