# 230. Kth Smallest Element in a BST

🔗 **Link:** [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can i use additional data structures like a list? -> yes
  
- Naive Solution:
  - put bst in a list and returns the kth index

### Match
- Problem Type: **Binary Search Trees**  
- Strategies:
  - **Binary Search Trees**: inorder traversal

### Plan
General idea:  
- Iterative idea:
- use stack and cur ptr
- 1. add to stack, keep going left (until null)
- 2. pop(), decrement `k`
- 3. go to pop().right

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


