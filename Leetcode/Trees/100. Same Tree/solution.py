# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Time: O(n) | Space: O(h)
        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False

            # recursively check if left and right subtree are 'Same'
            l = dfs(p.left, q.left)
            r = dfs(p.right, q.right)

            return l and r

        return dfs(p, q)
