# 226. Invert Binary Tree

🔗 **Link:** [Invert Binary Tree] (https://leetcode.com/problems/invert-binary-tree/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - how can we invert an Null or node with no children? -> return it

### Match
- Problem Type: **Binary Tree**  
- Strategies:
  - **Binary Tree**: Recursion, recurse down the tree with swap.

### Plan
General idea:  
- Base case: if root == None: return None
- swap root.left, root.right
- recurse down the whole tree

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N=#of Nodes)  
- **Space Complexity:** O(H=height of tree)  

---


