# 704. Binary Search

🔗 **Link:** [Binary Search](https://leetcode.com/problems/binary-search/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - no
  
- Naive Solution:
  - for loop to check all elements
  - O(n) time

### Match
- Problem Type: **Binary search**  
- Strategies:
  - **Binary search**: 

### Plan
General idea:  
- l, r both ends of the array
- while l <= r
  - mid = l + (r - l) // 2
  - compare nums[mid] to target
  - update l, r accordingly

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(logN)  
- **Space Complexity:** O(1)  

---


