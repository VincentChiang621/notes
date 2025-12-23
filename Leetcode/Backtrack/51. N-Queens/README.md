# 51. N-Queens

🔗 **Link:** [N-Queens](https://leetcode.com/problems/n-queens/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - is it possible to have no solutions to nqueens? -> yes for n=2, n=3

### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: dfs into each column, dont need to track rows

### Plan
General idea:  
- cols, posDiag, negDiag = set()
- posDiag = r + c, negDiag = r - c
- go deeper into dfs then pop that r,c when we finish looking at it
- basecase: if c in cols, r + c in posDiag, r - c in negDiag 

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  
- ✅ Pros: Fast lookup with hashmap.  
- ❌ Cons: Extra memory usage.  

---



