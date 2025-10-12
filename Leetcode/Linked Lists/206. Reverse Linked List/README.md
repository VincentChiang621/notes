# 206. Reverse Linked List

🔗 **Link:** [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can linked list be empty

### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: keep track of prev ptr and nxt ptr.

### Plan
General idea:  
- Iterative:
  - cur ptr points to current pointer we're working on, nxt ..., prev ...
  - 1. stores nxt = curr.next ptr
  - 2. cur.next points to prev
  - 3. prev = cur, because we lost reference to prev.next
  - 4. cur = nxt, because we lost reference to cur.next

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


