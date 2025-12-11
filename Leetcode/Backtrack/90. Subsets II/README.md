# 90. Subsets II

🔗 **Link:** [Subsets II](https://leetcode.com/problems/subsets-ii/description/)  
💡 **Difficulty:** Medium  

---

## UMPIRE Method

### Understand
- Clarifying questions:
  - is nums sorted -> no
  

### Match
- Problem Type: **Set + Backtrack**  
- Strategies:
  - **Set**: Stores the duplicate nums 
  - **Backtrack**: append then pop()

### Plan
General idea:  
- create res for return
- add to res any answer
- use parameter bt(i=int, arr=[])  
- base case: i == len(nums)

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N * 2^N)  
- **Space Complexity:** O(N)  


---