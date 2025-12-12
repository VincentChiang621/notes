# 40. Combination Sum II

🔗 **Link:** [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - candidates can have duplicates -> yes
  
- Naive Solution:
  - backtrack() to add or not add candidates[i]

### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: add or not add, skip overlaps

### Plan
General idea:  
- Basecase: sum > target | i > len(candidates) | sum == target
- append candidate[i] -> recurse -> pop()
- while loop to skip repeating [1,1,1,1,1,1,1,1,1,1], target = 20 -> we dont need to look at same 1s
- recurse with no appends

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N*2^N)  
- **Space Complexity:** O(N)   

---



