# 78. Subsets

🔗 **Link:** [Subsets](https://leetcode.com/problems/subsets/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - is a [] part of the subset? yes
  - does the order of the subsets matter? no

### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: Only can use brute force 

### Plan
General idea:  
- initialize result arr
- use backtrack algorithm
- use .copy(), also pop after appending to new dfs() call


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N*2^N)  
- **Space Complexity:** O(N)  

---


