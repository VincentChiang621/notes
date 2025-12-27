# 684. Redundant Connection

🔗 **Link:** [Redundant Connection](https://leetcode.com/problems/redundant-connection/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - 

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: union find 

### Plan
General idea:  
- find() with path compression and union() with rank
- whenever we try to union two same parents, then we detected a cycle!

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


