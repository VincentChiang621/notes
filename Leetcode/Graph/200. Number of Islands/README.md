# 200. Number of Islands

🔗 **Link:** [Number of Islands](https://leetcode.com/problems/number-of-islands/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can grid be empty? no

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: bfs or dfs to fill our visited set().

### Plan
General idea:  
- use visited set()
- for every cell, check not visited and grid[][] == '1', then we do our dfs() or bfs()
- count how many times we begin filling our visited

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(m*n)  
- **Space Complexity:** O(m*n)   

---


