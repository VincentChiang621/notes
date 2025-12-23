# 133. Clone Graph

🔗 **Link:** [Clone Graph](https://leetcode.com/problems/clone-graph/description/)  
💡 **Difficulty:** Medium  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Will there be any cycles? -> no


### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: use dfs() or bfs(), create the clone first mapped to hashmap 

### Plan
General idea:  
- Create a hashmap to store oldToNew nodes
- 1. create the node if not created
- 2. make the connection to its neighbors

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


