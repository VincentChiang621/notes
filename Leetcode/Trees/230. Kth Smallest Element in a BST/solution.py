# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Recursive
        # Time: O(N) | Space: O(H)
        kth = root.val

        def inorder(root):
            nonlocal kth, k
            if root == None:
                return 

            inorder(root.left)

            if k == 0:
                return
            # at the smallest:
            k -= 1
            kth = root.val

            inorder(root.right)

        inorder(root)
        return kth
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Iterative
        # Time: O(N) | Space: O(H)
        stack = []
        cur = root

        while True:
            # process lefts
            while cur:
                stack.append(cur)
                cur = cur.left

            # k-th smallest rn
            res = stack.pop()
            k -= 1
            if k == 0:
                return res.val

            # process rights
            cur = res.right
