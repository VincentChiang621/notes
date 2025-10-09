# 153. Find Minimum in Rotated Sorted Array

🔗 **Link:** [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can the `nums` array be empty?  
  
- Naive Solution:
  - check every element to see minimum
  - O(N) too time inefficient

### Match
- Problem Type: **Binary Search**  
- Strategies:
  - **Binary Search**: since sorted, we can cut inputs in half with some properties

### Plan
General idea:  
- initialize l, r
- while l <= r
  - mid = (l + r) // 2
  - if LEFT sorted:
    - take nums[l] and update l
  - else (RIGHT sorted):
    - take nums[m] and update r


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(logN)  
- **Space Complexity:** O(1)  

---


