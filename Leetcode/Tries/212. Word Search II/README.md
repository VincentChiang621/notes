# 212. Word Search II

🔗 **Link:** [Word Search II](https://leetcode.com/problems/word-search-ii/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - The word search can only go left right up down right? Also can it take the same chars by going left right left right?
  - Input: List[List[str]], List[str] → Output: List[str]

  
- Naive Solution:
  - I can just check run a search on every word in `words`
  - Do a dfs on every word on the `board`
  - Need to run through every letter in the board and a dfs() search on all
  - Time: O(n * m * L=len(words) * 4^L)


### Match
- Problem Type: **Tries**  
- Strategies:
  - **Tries**: Prefix tree to help prune backtracking algorithm

### Plan
General idea:  
- Prefix tree on the `words`
- loop the `board`
  - use backtrack on `board[r][c]` 
  - base cases + check if in tree.children
  - append to res once at end

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N*M*4^L)  
- **Space Complexity:** O(N)  

---


