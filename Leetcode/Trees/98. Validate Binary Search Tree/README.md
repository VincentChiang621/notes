# 98. Validate Binary Search Tree

🔗 **Link:** [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - n/a

### Match
- Problem Type: **Binary Search Trees**  
- Strategies:
  - **Binary Search Trees**: pass in the 'range' each node can have, check its validity 

### Plan
General idea:  
- base case: if root == None: return True
- base case: if root.val not bounded by `lbound` and `rbound`: return False
- recursively returns whether left and right are BST

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


