# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# serialize(self, root): makes tree structure into a string
# deserialize(self, data): makes string into tree structure

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # encodes to Level order traversal:
        res = []

        def dfs(root):
            if not root:
                res.append("N")
                return

            res.append(str(root.val))
            l = dfs(root.left)
            r = dfs(root.right)

        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree = data.split(",")
        ind = 0

        def dfs():
            nonlocal ind
            if tree[ind] == "N":
                ind += 1
                return None

            root = TreeNode(str(tree[ind]))
            ind += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))