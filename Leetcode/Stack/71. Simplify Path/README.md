# 71. Simplify Path

🔗 **Link:** [Simplify Path](https://leetcode.com/problems/simplify-path/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Input: “/./”
  - Output: “/”

  - Input: “/a/b/../”
  - Output: “/a”

  - Input: “////ab////”
  - Output: “/ab”

  - Input: “/…/…”
  - Output: “/…/…”

  - Input: “/”
  - Output: “/”

  - Input: “/a/.”
  - Output: “/a”


### Match
- Problem Type: **Stack**  
- Strategies:
  - **Stack**: LIFO ordering of directories, store all directories in a []

### Plan
General idea:  
- Sounds like directories = stack() LIFO 
- Use a stack to store directories anything not '.' or '..'
- If we get '.' → then don't do anything to the stack
- Elif '..' → remove one directory from stack (if any)
- Use the split(‘/’) to make processing easier


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


