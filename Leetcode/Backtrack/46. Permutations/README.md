# 46. Permutations

🔗 **Link:** [Permutations](https://leetcode.com/problems/permutations/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - how to handle same elements? only distinct ints

### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: brute force ALL permutations

### Plan
General idea:  
- dfs(subarray)
- if size == nums:
-   append to result
- go through all elements:
- if not added, add to sub

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N * N!)  
- **Space Complexity:** O(N)  

---


