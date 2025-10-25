# 572. Subtree of Another Tree

🔗 **Link:** [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - root or subRoot be empty -> no


### Match
- Problem Type: **Binary Tree**  
- Strategies:
  - **Binary Tree**: Check at every node of root whether we have a sameTree

### Plan
General idea:  
- helper isSameTree(r,s) to compare whether r and s are same tree
- call that on every node of root, using DFS to traverse down
- returns whether root is same tree OR left subtree sameTree OR right subtree sameTree

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N^2)  
- **Space Complexity:** O(H)  

---


