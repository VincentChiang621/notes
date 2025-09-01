class Solution:
    def trap(self, height: List[int]) -> int:
        # Naive Solution
        # Time: O(n^2) | Space: O(1)
        res, l_max = 0, height[0]
        
        for i in range(1, len(height)):
            # get the right highest
            r_max = 0
            for j in range(i + 1, len(height)):
                r_max = max(r_max, height[j])

            # now we add to res if we can fit water at ind 'i'
            water = min(l_max, r_max) - height[i]
            res += water if water > 0 else 0

            l_max = max(l_max, height[i])

        return res

    def trap(self, height: List[int]) -> int:
        # Precomputed left and right highest array approach
        # Time: O(n) | Space: O(n)
        n = len(height)
        h_left, h_right = [0] * n, [0] * n

        for i in range(1, n):
            h_left[i] = max(h_left[i - 1], height[i - 1])

        for j in range(n-2, -1, -1):
            h_right[j] = max(h_right[j + 1], height[j + 1])

        trapped = 0
        for k in range(n):
            water = min(h_left[k], h_right[k]) - height[k]
            trapped += water if water > 0 else 0

        return trapped

    def trap(self, height: List[int]) -> int:
        # Time: O(n) | Space O(1)
        n, res = len(height), 0
        l_max, r_max = height[0], height[n - 1]
        l, r = 1, n - 2

        while l <= r:
            if l_max < r_max:
                # we are limited by left side
                water = min(l_max, r_max) - height[l]
                l_max = max(l_max, height[l])
                l += 1
            else:
                # limited by right side OR same so just pick one
                water = min(l_max, r_max) - height[r]
                r_max = max(r_max, height[r])
                r -= 1

            # add water only if positive
            res += water if water > 0 else 0

        return res

