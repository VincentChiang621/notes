# 141. Linked List Cycle

🔗 **Link:** [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - head be empty?
  
- Naive Solution:
  - run a loop for the linked list and check for duplicates with set()
  - takes O(n) time and O(n) space

### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: two pointers --> slow and fast pointer

### Plan
General idea:  
- initialize fast and slow pointer at head
- move fast.next.next and slow.next,
- if there is a cycle, they will eventually meet up

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


