# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Time: O(n) | Space: O(n)
        cur = 0

        def dfs(inorder):
            nonlocal cur

            if not inorder:
                return None
            
            ind = inorder.index(preorder[cur])
            root = TreeNode(preorder[cur])
            cur += 1

            root.left = dfs(inorder[:ind])
            root.right = dfs(inorder[ind+1:])

            return root

        return dfs(inorder)