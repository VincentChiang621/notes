# 261. Graph Valid Tree

🔗 **Link:** [Graph Valid Tree](https://leetcode.com/problems/graph-valid-tree/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - 

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**: bfs/dfs and to detect a cycle with (undirected)

### Plan
General idea:  
- 1. bfs()
- undirected edges adjMat[] goes both ways
- in the bfs() track the prev in queue, (node, prev)
- 2. Union Find
- make union() with rank and find()
- when we try to union two components with same parent: we return False right away
- else we return if (n-1) == len(edges), meaning a fully connected graph

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


