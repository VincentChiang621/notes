# 100. Same Tree

🔗 **Link:** [100. Same Tree](https://leetcode.com/problems/same-tree/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can `p` or `q` be empty?

### Match
- Problem Type: **Binary Trees**  
- Strategies:
  - **Binary Trees**: DFS to look into every node, recursively check if all children are "same"

### Plan
General idea:  
- base case: if both p, q = None: return True
- base case: if only one of p or q is None: return False
- base case: if p.val != q.val: return False
- recursive check both left and right subtree
- returns whether left and right are EQUAL

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


