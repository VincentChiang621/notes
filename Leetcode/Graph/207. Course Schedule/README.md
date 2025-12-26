# 207. Course Schedule

🔗 **Link:** [Course Schedule](https://leetcode.com/problems/course-schedule/description/)  
💡 **Difficulty:** Medium 

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can we have repeating array[i]? no

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: can use bfs/dfs for cycle detection, also topological sort

### Plan
General idea:  
- 1. DFS() 
- make adjMatrix
- everytime we visit a course, we can pop it off 
- use a visited set()
- 2. Topological Sort
- count how many incoming (degrees)
- initialize q with those with no prerequisites
- free up degrees with those courses taken, update q with no degrees

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N + M)  
- **Space Complexity:** O(N + M)  

---


