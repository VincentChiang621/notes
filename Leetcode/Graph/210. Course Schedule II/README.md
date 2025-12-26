# 210. Course Schedule II

🔗 **Link:** [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)  
💡 **Difficulty:** Medium  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - 

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: Topological Sort

### Plan
General idea:  
- make in-degree list (how many prereqs does crs[i] have)
- make free map, free up in-degrees after taking crs[i] 
- initialize Queue with in-degrees == 0
- keep looking and freeing up degrees, add to queue when indegrees == 0

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N + M)  
- **Space Complexity:** O(N + M)  

---


