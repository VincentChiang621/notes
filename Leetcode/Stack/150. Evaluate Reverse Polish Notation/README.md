# 150. Evaluate Reverse Polish Notation

🔗 **Link:** [valuate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Are we guaranteed that the number of operations are == # numbers - 1?
  - What about an empty input?
  - Input = [‘3’]

### Match
- Problem Type: **Stack**  
- Strategies:
  - **Stack**: push(x) and pop() in both O(1) time, and its LIFO nature fits problem statement


### Plan
General idea:  
- I would like to use a number stack to store integers
- Keep pushing integers into my stack
- When i see operation:
    - Pop two LIFO elements: preform that operation on them
    - Push the result back into the stack
    - In the end, return the sole value inside the stack. Guaranteed to be only 1 left because of the it is guaranteed to be a valid polish notation.

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


