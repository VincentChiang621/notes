# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time: O(n) | Space: O(h)
        max_diameter = 0

        # returns height
        def dfs(root):
            if not root:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            nonlocal max_diameter
            max_diameter = max(l + r, max_diameter)
            return max(l, r) + 1

        dfs(root)
        return max_diameter