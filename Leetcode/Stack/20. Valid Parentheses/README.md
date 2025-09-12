# 20. Valid Parentheses

🔗 **Link:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can `s` be empty
  - What chars are `s` guarenteed to be

### Match
- Problem Type: **Stack**  
- Strategies:
  - **Stack**: ✅ A good datastructure because we want to use Last In First Out LIFO.

### Plan
General idea:  
- use a stack by `[]` in python, pop() and stack[-1]
- if open parentheses: add to stack
- else: check if can pop(), if not, return false
- return whether stack is empty

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


