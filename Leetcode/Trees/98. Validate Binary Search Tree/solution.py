# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lbound, rbound):
            if root == None:
                return True
            elif root.val >= rbound or root.val <= lbound:
                return False

            l = dfs(root.left, lbound, root.val)
            r = dfs(root.right, root.val, rbound)

            return l and r

        return dfs(root, float('-inf'), float('inf'))
