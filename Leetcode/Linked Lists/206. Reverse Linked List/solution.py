# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative
        # Time: O(n) | Space: O(1)
        prev, cur = None, head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive
        # Time: O(n) | Space O(N)
        def reverse(prev, head):
            if not head:
                return prev
            
            nxt = head.next
            head.next = prev

            return reverse(head, nxt)

        return reverse(None, head)
    
