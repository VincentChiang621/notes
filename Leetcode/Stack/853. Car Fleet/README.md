# 853. Car Fleet

🔗 **Link:** [Car Fleet](https://leetcode.com/problems/car-fleet/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can cars start at the same position? each pos[i] is unique
  - 
  
- Naive Solution:
  - Run a nested for loop and check each element to see if match
  - Problem -> repeated work for checking... 

### Match
- Problem Type: **Sorting + Stack**  
- Strategies:
  - **Sorting**: sort by [position, speed]
  - **Stack**: 

### Plan
General idea:  
- Do a `steps` list [steps, pos] to track how much ‘time’ it would take for each pos[i] to reach target
- 

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(NlogN)  
- **Space Complexity:** O(N)  

---


