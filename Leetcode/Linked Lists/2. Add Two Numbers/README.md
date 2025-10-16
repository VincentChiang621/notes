# 2. Add Two Numbers

🔗 **Link:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can l1 or l2 be empty -> no
  - are we allowed to create new nodes -> yes
  
- Naive Solution:
  - Iterate both l1 and l2 and store all node values in a string
  - Then reverse the string to make it the correct integer values
  - Then add those two values
  - Create the LL in reverse order based on the added value
  - O(n) time and O(n) space to store string


### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: iterate LL also with a `carry`

### Plan
General idea:  
- Start pointer at beginning of l1 and l2 (go from smallest to larger digit)
- maintain a `carry` variable to track if this addition goes overflow
- remember to add the value % 10 and track `carry`

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


