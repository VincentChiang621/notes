# 19. Remove Nth Node From End of List

🔗 **Link:** [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can we have head == None?
  - Is it guaranteed that n >= 1 and smaller than the length of LL?

  
- Naive Solution:
  - Put the whole linked list in an array
  - Then go to the index before last n and remove the links 
  - O(n) time and O(n) space



### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: two pointer approach, l is `n` steps slower than r

### Plan
General idea:  
- use a dummy = ListNode(0, head)
- update r to be `n` steps ahead (from head)
- then run both l and r = .next
- once r has no more .next(), we can remove l.next = l.next.next

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


