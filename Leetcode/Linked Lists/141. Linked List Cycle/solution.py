# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head:ListNode) -> bool:
        # Time: O(n) | Space: O(1)
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

class Solution:
    def hasCycle(self, head:ListNode) -> bool:
        # use a dummy and set the ptr.next to dummy after traversal
        # ONLY USE if allowed to change original Linked List
        # Time: O(n) | Space: O(1) 
        dummy = ListNode(-1)

        ptr = head
        while ptr:
            if ptr == dummy:
                return True

            tmp = ptr.next
            ptr.next = dummy
            ptr = tmp

        return False