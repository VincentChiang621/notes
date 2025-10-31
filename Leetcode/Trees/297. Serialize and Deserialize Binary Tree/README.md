# 297. Serialize and Deserialize Binary Tree

🔗 **Link:** [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Are duplicate node values allowed in the tree? -> yes
  - do we need to handle empty trees? -> yes

### Match
- Problem Type: **Binary Trees**  
- Strategies:
  - **Binary Trees**: dfs traversal for serialization and deserialization

### Plan
General idea:  
- serialize: 
  - remember to track null nodes
  - use preorder DFS
- deserialize:
  - global tracker on index
  - remember to update even when its 'NULL'

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


