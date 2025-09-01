class Solution:
    def threeSum(self, nums:List[int]) -> List[List[int]]:
        # Time: O(n^3) | Space: O(n)
        nums.sort()
        res = []

        for i in range(len(nums) - 2) :
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append((nums[i], nums[j], nums[k]))

        return list(set(res))
    
    def threeSum(self, nums:List[int]) -> List[List[int]]:
        # Time: O(n^2) | Space: O(n) or O(1), depends on .sort() implementation
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            # skip over duplicates
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            # two pointers since sorted 
            j, k =  i + 1, len(nums) - 1
            while j < k:
                tar = nums[i] + nums[j] + nums[k]
                if tar < 0:
                    j += 1
                elif tar > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                
        return res