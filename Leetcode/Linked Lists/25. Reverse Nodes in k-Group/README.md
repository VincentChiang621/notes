# 25. Reverse Nodes in k-Group

🔗 **Link:** [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - how do you reverse when k = 1 -> return original list
  - are we just manipulating pointers instead of creating new nodes? - > yes
  

### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: pointer manipulation

### Plan
General idea:  
- use a dummy node
- keep track of the next pointer after reversal (will lose it if just reverse)
- 0. reverse k times (for loop)
- 1. connect the old head with reversed `prev`
- 2. update old head to new head (beginning of reversed LL)

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


