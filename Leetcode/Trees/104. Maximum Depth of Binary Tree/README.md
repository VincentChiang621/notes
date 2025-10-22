# 104. Maximum Depth of Binary Tree

🔗 **Link:** [Maximum Depth of Binary Tree](https://link.com)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Is there a difference between depth of the tree and height?
  - What is the max depth of a tree with no nodes?

### Match
- Problem Type: **Binary Tree**  
- Strategies:
  - **Binary Tree**: Recursion, use 1 + max(left subtree, right subtree)

### Plan
General idea:  
- Base case: if root == None: return 0
- return 1 + max(left subtree, right subtree) 

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


