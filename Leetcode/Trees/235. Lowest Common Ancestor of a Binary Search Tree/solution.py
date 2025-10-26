# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # This just searches for LCA of a Binary Tree
        # Time: O(n) | Space: O(h)
        res = None
        def dfs(root):
            # return value: [p_found, q_found]
            if root is None:
                return [False, False] 
            p_found = True if root == p else False
            q_found = True if root == q else False

            l = dfs(root.left)
            r = dfs(root.right)

            p_found = p_found or l[0] or r[0]
            q_found = q_found or l[1] or r[1]

            nonlocal res
            if p_found and q_found and res == None:
                res = root

            return [p_found, q_found]

        dfs(root)
        return res

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time: O(h) | Space: O(h)
        def search(root, p, q):
            # base: when root is in range [p.val, q.val]
            if p.val <= root.val <= q.val:
                return root
            elif root.val < p.val:
                return search(root.right, p, q)
            else:
                return search(root.left, p, q)

        # p.val is always smaller than q.val
        if p.val > q.val:
            p, q = q, p

        return search(root, p, q)
    