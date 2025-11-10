# 1405. Longest Happy String

🔗 **Link:** [Longest Happy String](https://leetcode.com/problems/longest-happy-string/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - if we found a longest happy string, can we assume its unique? it doesn't have to be, return an arbitrary one

  
### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: maxHeap for counter [a, 'a'], [b, 'b'], [c, 'c']

### Plan
General idea:  
- make maxHeap counter
- always take the letter with most letters first
- 'GREEDY APPROACH'

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N=a+b+c)  
- **Space Complexity:** O(1)  


---


