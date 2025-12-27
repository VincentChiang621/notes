# 323. Number of Connected Components in an Undirected Graph

🔗 **Link:** [Number of Connected Components in an Undirected Graph](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/)  
💡 **Difficulty:** Medium 

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can we have duplicate edges[i] -> no

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: bfs() to fill out visited set()

### Plan
General idea:  
- 1. bfs or dfs: 
- keep filling out a visited set and maintain count
- update count += 1 whenever we call another bfs() 
- only call bfs if that node is not in visited
- 2. union find:
- rank = [] and parent = []
- fill out parent and union() based on rank
- use path compression on find()

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


