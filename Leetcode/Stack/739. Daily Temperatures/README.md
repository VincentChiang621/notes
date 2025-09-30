# 739. Daily Temperatures

🔗 **Link:** [Daily Temperatures](hhttps://leetcode.com/problems/daily-temperatures/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - [55,54,53,52,51] → [0,0,0,0,0]
  - Empty input outputs []?
  - [50,55,53,59,58] → [1,2,1,0,0]
  - [55,53,52,53,60] → [4,3,1,1,0]

  
- Naive Solution:
  - run nested for loop
  - O(N^2)

### Match
- Problem Type: **Stack**  
- Strategies:
  - **Stack**: monotonic decreasing stack, [temp, ind] 

### Plan
General idea:  
- monotonic stack
- while stack and stack[-1][0] < n:
    - pop from stack
    - update res
- append([temp, ind])

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

- Each element is poped and pushed from the stack at most once
- push and pop in stack is only O(1)


---


