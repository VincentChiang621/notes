# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Time: O(n) | Space: O(1)
        def getKNext(head):
            for i in range(k):
                head = head.next if head else head

            return head

        dummy = ListNode(0, head)
        cur = dummy
        
        while True:
            prev = getKNext(cur)
            if prev == None:
                break

            prev = prev.next

            # reverse k times:
            start, nextStart = cur.next, cur.next
            for i in range(k):
                nxt = start.next
                start.next = prev
                prev = start
                start = nxt

            # connects last portions
            cur.next = prev
            cur = nextStart

        return dummy.next
            