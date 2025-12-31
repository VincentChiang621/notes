# 778. Swim in Rising Water

🔗 **Link:** [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/description/)  
💡 **Difficulty:** Hard 

---


## UMPIRE Method

### Understand
- Clarifying questions:
- Dijkstra's Algorithm

### Match
- Problem Type: **Advanced Graphs**  
- Strategies:
  - **Advanced Graphs**: Dijkstra's Algorithm

### Plan
General idea:  
- Dont need to explore every path: use greedy
- always keep picking the path that has the smallest depth.
- use BFS() but with a minHeap: end at (n-1, n-1)

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(n^2logn)  
- **Space Complexity:** O(n^2)  

---


