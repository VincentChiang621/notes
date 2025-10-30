# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time: O(n) | Space: O(h)
        res = root.val
        # returns the maxPath of left or right or itself
        def dfs(root) -> int: 
            nonlocal res

            if root == None:
                return 0

            l = dfs(root.left)
            r = dfs(root.right)

            onlyLeft = l + root.val
            onlyRight = r + root.val
            both = l + r + root.val

            res = max(res, root.val, onlyLeft, onlyRight, both)

            return max(onlyLeft, onlyRight, root.val)           

        dfs(root)
        return res