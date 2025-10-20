# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time: O(Nlogk) = O(totalNodes * log(len(lists)))
        # Space: O(k)
        minHeap = []
        uid = 0

        for li in lists:
            if li:
                minHeap.append([li.val, uid, li])
                uid += 1

        heapq.heapify(minHeap)
        
        dummy = ListNode()
        cur = dummy

        while minHeap:
            _, _, cur.next = heapq.heappop(minHeap)
            cur = cur.next
            if cur.next:
                heapq.heappush(minHeap, [cur.next.val, uid, cur.next])
                uid += 1

        return dummy.next