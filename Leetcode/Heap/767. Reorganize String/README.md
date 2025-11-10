# 767. Reorganize String

🔗 **Link:** [Reorganize String](https://leetcode.com/problems/reorganize-string/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Is there a specific arrangement I should return if we have duplicate answers?
  
### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: maxHeap to track [freq, char]

### Plan
General idea:  
- create counter, then use that to make maxHeap
- while maxHeap:
  - if 'aa', 'bb', ...,:
    - use the second mostFreq if possible
  - else:
    - use the first and heappush[freq+1,val]

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


