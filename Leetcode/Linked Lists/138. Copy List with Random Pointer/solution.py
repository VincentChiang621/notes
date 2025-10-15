"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Time: O(n) | Space: O(n)
        # 1st pass -> make the deep copies and map to nodeMap
        nodeMap = {None: None}
        i = head
        while i:
            nodeMap[i] = Node(i.val, None, None)
            i = i.next

        # 2nd pass -> connect the random pointers
        i = head
        while i:
            nodeMap[i].next = nodeMap[i.next]
            nodeMap[i].random = nodeMap[i.random]
            i = i.next

        return nodeMap[head]