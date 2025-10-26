# 235. Lowest Common Ancestor of a Binary Search Tree

🔗 **Link:** [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - are p and q guarenteed to be in the BST? -> yes
  - can root be None? -> root will at least contain 2 nodes
  
- Naive Solution:
  - run DFS on the tree 
  - dont use the sorted property of BST
  - Time O(n) | Space: O(h)
  - (implemented in solution.py)

### Match
- Problem Type: **BST**  
- Strategies:
  - **BST**: iterative or recursively run search on BST

### Plan
General idea:  
- if root.val is in between p and q, then that is the LCA
- if root.val > p and q, then we need to look left
- if root.val < p and q, then we need to look right

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(logN = h)  
- **Space Complexity:** O(1) if iterative

---


