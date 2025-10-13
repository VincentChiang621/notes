# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # use array to get index of listnodes
        # Time: O(n) | Space: O(n)
        arr = []
        i = head
        while i:
            arr.append(i)
            i = i.next

        l, r = 0, len(arr) - 1
        while l < r:
            arr[l].next = arr[r]
            l += 1

            arr[r].next = arr[l]
            r -= 1

        arr[l].next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time: O(n) | Space: O(1)
        # helper for part1
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            
            return prev
        
        # 1. reverse the second half of LL
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next

        r = reverse(s)

        # 2. connect the pointers
        l = head
        while r.next:
            # Connect L0 to Ln
            lnxt = l.next
            l.next = r
            l = lnxt

            # Connnect Ln to L1
            rnxt = r.next
            r.next = l
            r = rnxt

        return head