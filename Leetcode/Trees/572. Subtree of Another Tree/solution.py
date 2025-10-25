# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # Time: O(n^2) | Space: O(height(root))
        def isSameTree(first, second):
            if not first and not second:
                return True
            elif not first or not second:
                return False
            elif first.val != second.val:
                return False

            l = isSameTree(first.left, second.left)
            r = isSameTree(first.right, second.right)
            return l and r

        def dfs(root):
            if not root:
                return False

            same = isSameTree(root, subRoot)
            l = dfs(root.left)
            r = dfs(root.right)

            return same or l or r

        return dfs(root)
