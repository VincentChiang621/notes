# 543. Diameter of Binary Tree

🔗 **Link:** [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - what is diameter of null or node with no children --> 0 

- Naive Solution:
  - Check the max diameter with every node as the root, 
  - Time: O(n^2) Space: O(n)

### Match
- Problem Type: **Binary Trees**  
- Strategies:
  - **Binary Trees**: DFS returns height, updates max_diameter variable

### Plan
General idea:  
- base: if root == None: return 0
- returns height for left and right to calculate/update max_diameter
- height = max(left, right) + 1

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


