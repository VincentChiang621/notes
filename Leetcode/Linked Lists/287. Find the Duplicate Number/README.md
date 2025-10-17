# 287. Find the Duplicate Number

🔗 **Link:** [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can we assume we have len(nums) = n + 1 and values of nums can only be [1,n]
  
- Naive Solution:
  - Since each number in nums is in range [1,n] we can start at index 0 and check the value of it
  - Each value would be a valid index of the array
  - I can just traverse the array with the next index being the value of that number
  - The duplicate index traveled would be our result, maybe track this by changing every traversed index into ‘-1’
  - Problem: We cannot change content of the input

### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: Cycle detection -> detect start of cycle

### Plan
General idea:  
- 1. Detect cycle: slow and fast pointers
- 2. Find cycle start: start another ptr at the head

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


