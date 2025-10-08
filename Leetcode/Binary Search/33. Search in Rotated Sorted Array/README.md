# 33. Search in Rotated Sorted Array

🔗 **Link:** [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can array be empty? 
  
- Naive Solution:
  - check every element and find if target in array
  - O(N) takes too long

### Match
- Problem Type: **Binary Search**  
- Strategies:
  - **Binary Search**: conditions to see whether you match or not 

### Plan
General idea:  
- LEFT and RIGHT sorted portionrs
- if in left, check if target within left
    - move pointers
- else
    - move pointers

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(logN)  
- **Space Complexity:** O(1)  

---


