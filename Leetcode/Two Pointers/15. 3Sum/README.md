# 15. 3Sum

🔗 **Link:** [3Sum](https://leetcode.com/problems/3sum/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can nums[i], nums[j], nums[k] all == 0?
  - Are we guaranteed a solution? What if all elements are positive non-zero numbers (or negative)?
      - No, if no solution: return []
  - What should I return if there are multiple solutions?
      - return a list of distinct solutions

- Naive Solution:
  - nums.sort()
  - three pointers to run nested nested for loops
  - If nums[i] + nums[j] + nums[k] == 0: append to result
  - Run a set() on result to ensure distinct answers
  - O(n^3)

### Match
- Problem Type: **Sorting + Two Pointers**  
- Strategies:
  - **Two Pointers**: ✅ Useful since nums.sort(), see Two Sum II
  - **Sorting**: ✅ Efficient and useful because we just want distinct numbers 

### Plan
General idea:  
- nums.sort()
- Outer loop goes though every element (i)
- Inner loop does two pointers l = i + 1, r = len(nums) - 1 and appends to l or r with comparison to target == 0
- Since two pointer approach only costs O(n)= this function is then O(n^2) and sorting (negligible) 


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N^2)  
- **Space Complexity:** O(1) or O(N), depends on .sort() implementation 

---


