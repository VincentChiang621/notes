# 743. Network Delay Time

🔗 **Link:** [Network Delay Time](https://leetcode.com/problems/network-delay-time/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Dijkstra's Algorithm
  

### Match
- Problem Type: **Advanced Graphs + minHeap**  
- Strategies:
  - **Advanced Graphs + minHeap**: BFS algorithm with minHeap [weight_i, node_i]

### Plan
General idea:  
- make the adjMatrix = src_node -> [[tar_node, weight], ...etc,]

- Dijkstra's Algorithm:
- first

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(E + log(V))  
- **Space Complexity:** O(E)  

---


