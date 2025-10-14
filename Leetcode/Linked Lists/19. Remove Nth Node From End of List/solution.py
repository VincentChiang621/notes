# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head:ListNode(), n:int) -> ListNode():
        # One Pass
        # Time: O(n) | Space: O(1)
        dummy = ListNode()
        dummy.next, res = head, dummy

        l, r = dummy, dummy

        # move right pointer n forward
        for i in range(n):
            r = r.next

        # r is n moves ahead of l
        while r.next:
            r = r.next
            l = l.next

        # l is at 1 behind victim node: remove the victim
        l.next = l.next.next

        return res.next