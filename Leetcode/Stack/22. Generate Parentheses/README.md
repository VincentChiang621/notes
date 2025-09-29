# 22. Generate Parentheses

🔗 **Link:** [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)  
💡 **Difficulty:** Medium  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Does the order of the output matter? no
  - Based on my understanding, well formed means all open paren has a closing? yes
  - The n represents the pairs of parentheses? yes
  - N = 2 → [“(())”, “()()”]

### Match
- Problem Type: **DFS + Stack**  
- Strategies:
  - **Stack**: stores res
  - **DFS**: two options, add "(" or ")" and store openP and closeP

### Plan
General idea:  
- Firstly, start with an opening "("
- Choose two paths, add "(" or ")", always go two ways
- Prune the paths where not possible "())", more closing than opening
- I would want to track counts
    - Base case: when open == close == n: append to res
    - Append to both sides
    - Prune off when close > open


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(2^N)
- **Space Complexity:** O(N)  

---


