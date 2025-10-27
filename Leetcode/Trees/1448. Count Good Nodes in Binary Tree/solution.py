# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS recursion postorder
        # Time: O(n) | Space: O(h)
        def dfs(root, maxVal):
            if not root:
                return 0

            l = dfs(root.left, max(maxVal, root.val))
            r = dfs(root.right, max(maxVal, root.val))
            
            if root.val >= maxVal:
                return l + r + 1

            return l + r

        return dfs(root, root.val)

    def goodNodes(self, root: TreeNode) -> int:
        # BFS 
        # Time: O(n) | Space: O(n)
        q = deque([(root, root.val)])
        res = 0

        while q:
            for i in range(len(q)):
                cur, maxVal = q.popleft()
                res += 1 if cur.val >= maxVal else 0

                if cur.left:
                    q.append((cur.left, max(cur.val, maxVal)))
                if cur.right:
                    q.append((cur.right, max(cur.val, maxVal)))
                
        return res

