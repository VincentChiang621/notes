# 110. Balanced Binary Tree

🔗 **Link:** [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - is a null tree balanced? --> yes
  
### Match
- Problem Type: **Binary Tree**  
- Strategies:
  - **Binary Tree**: use DFS to return height, use that as a conditional to check if balanced

### Plan
General idea:  
- base: if root == None: return 0
- DFS returns height, use that return value to check if balanced
- updates res to False whenever we found a non-balanced.

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


