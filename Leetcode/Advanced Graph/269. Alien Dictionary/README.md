# 269. Alien Dictionary

🔗 **Link:** [Alien Dictionary](https://leetcode.com/problems/alien-dictionary/description/)  
💡 **Difficulty:** Hard 

---


## UMPIRE Method

### Understand
- Clarifying questions:
- Dijkstra's Algorithm

### Match
- Problem Type: **Advanced Graphs**  
- Strategies:
  - **Advanced Graphs**: Topological Sort

### Plan
General idea:  
- compare two words at a time
  - the first letter difference we can know which letter is first
  - draw up a `inDegrees` and `frees` array
  - also deal with case of ['vincent', 'vince'] -> return false immediately
  - then just run a topological sorting


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(len(ALL word in words))  
- **Space Complexity:** O(1)  

---


