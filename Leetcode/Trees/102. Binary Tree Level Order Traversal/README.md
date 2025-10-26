# 102. Binary Tree Level Order Traversal

🔗 **Link:** [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - n/a 

### Match
- Problem Type: **Binary Trees**  
- Strategies:
  - **Binary Trees**: BFS

### Plan
General idea:  
- BFS Algorithm:
- 1. initialize q with root
- 2. while q not empty:
- 3a. traverse everything in q
- 3b. also adding cur.left and cur.right if applicable 
- 4. updates res with level

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


