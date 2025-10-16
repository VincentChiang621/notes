# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Time: O(n) | Space: O(1)
        res = ListNode()
        cur = res
        carry = 0

        while l1 or l2 or carry:
            fir = l1.val if l1 else 0
            sec = l2.val if l2 else 0
            total = fir + sec + carry
            if total >= 10:
                total %= 10
                carry = 1
            else:
                carry = 0

            cur.next = ListNode(total)
            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return res.next