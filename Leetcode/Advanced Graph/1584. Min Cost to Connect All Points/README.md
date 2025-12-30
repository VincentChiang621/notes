# 1584. Min Cost to Connect All Points

🔗 **Link:** [Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description/)  
💡 **Difficulty:** Medium  

---

## UMPIRE Method

### Understand
- Clarifying questions:
  - This is a Minimum Spanning Tree Question:
  - can use Kruskal or Prims 

### Match
- Problem Type: **Advanced Graphs**  
- Strategies:
  - **Advanced Graphs**: Use Kruskal's Algorithm + UnionFind for efficient cycle detection. 

### Plan
General idea:  
- created a complete graph
- use a minHeap to track the lowest distances, 
- Kruskals (Greedy):
- keep choosing the lowest distance (cost) edges
- but not choose edges that create cycle (no point of that edge...)
  - do this efficiently via UNIONFIND()

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- N = # edges
- **Time Complexity:** O(N^2 * log(N))  
- **Space Complexity:** O(N^2)  

---


