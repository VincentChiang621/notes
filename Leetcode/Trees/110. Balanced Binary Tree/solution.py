# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        # Time: O(n) | Space: O(h)
        res = True

        # returns height
        def dfs(root):
            if not root: 
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            balanced = abs(l - r) <= 1
            nonlocal res
            res = res and balanced

            return 1 + max(l, r)

        dfs(root)
        return res