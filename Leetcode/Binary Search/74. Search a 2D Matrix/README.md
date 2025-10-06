# 74. Search a 2D Matrix

🔗 **Link:** [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can `matrix` be empty? --> no
  
- Naive Solution:
  - check every element to check if exists
  - O(N*M)

### Match
- Problem Type: **Binary Search**  
- Strategies:
  - **Binary Search**: efficient for sorted arrays

### Plan
General idea:  
- find row in question:
  - edge: immediately return false if row out of range
- use simple binary search for that row

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(log(N*M))  
- **Space Complexity:** O(1)  

---


