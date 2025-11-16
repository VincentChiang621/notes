# 39. Combination Sum

🔗 **Link:** [Combination Sum]([https://link.com](https://leetcode.com/problems/combination-sum/description/))  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - how many times can we repeat a candidate[i] -> infinitely
  
### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: Brute force with DFS all the combination sums to target

### Plan
General idea:  
- initialize res
- add copy() when tar == curSum
- return if curSum > tar
- potentially prune when curSum > tar (if sorted)

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(2^N)  
- **Space Complexity:** O(N)  

---


