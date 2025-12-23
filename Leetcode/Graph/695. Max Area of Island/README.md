# 695. Max Area of Island

🔗 **Link:** [Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can grid == None: no, grid has at least len == 1

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: bfs or dfs to find island size, update res if possible

### Plan
General idea:  
- visited set to track already visited coordinates
- use dfs or bfs to track only grid[r][c] == 1

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(M*N)  
- **Space Complexity:** O(M*N)  

---


