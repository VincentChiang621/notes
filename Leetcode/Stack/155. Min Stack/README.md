# 155. Min Stack

🔗 **Link:** [Min Stack](https://leetcode.com/problems/min-stack/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Are the push, pop, top all in Stack/LIFO order? yes
- Is it fine to use data structures like Stacks or Queues or arrays? yes
- MinStack = [0,-2,-3,1,2], top() -> 2, pop() -> pops 2, then getMin() -> -3? yes

  
- Naive Solution:
  - use a stack and then loop everything to getMin
  - causes O(N) getMin

### Match
- Problem Type: **Stack**  
- Strategies:
  - **Stack**: Useful for top(), pop(), and push(val), clever to use extra stack to store minimum RN.

### Plan
General idea:  
- two stacks: self.stack, self.minStack
- self.minStack tracks the minimum at each index of self.stack

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(1)  
- **Space Complexity:** O(N)  

---


