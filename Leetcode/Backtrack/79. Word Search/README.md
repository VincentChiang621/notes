# 79. Word Search

🔗 **Link:** [Word Search](https://leetcode.com/problems/word-search/description/)  
💡 **Difficulty:** Medium  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can we reuse the letters? No

### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: brute force ALL possible paths

### Plan
General idea:  
- DFS() to look for the ind = index @ word[i] and the row, col
- base case: out of bounds, in path, not equal
- go left, right, up, down

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(n * m * 3^n)  
- **Space Complexity:** O(len(word))  

---



