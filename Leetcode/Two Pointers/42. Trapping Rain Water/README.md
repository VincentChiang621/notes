# 42. Trapping Rain Water

🔗 **Link:** [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Are all values in `height` guarenteed to be > 0
  - Can `height` be empty?
  - Corner cases:
      - What is the return value for when `height` are all same value ie: [8,8,8,8,8]

  
- Naive Solution:
  - Run a nested for loop
  - Outer loop checks water trapped at height[i]
  - Inner loop checks the tallest (from right)
  - record the water since we can get leftTallest and rightTallest
  - Time: O(n^2) | Space: O(1)

### Match
- Problem Type: **Two Pointers + Array**  
- Strategies:
  - **Array**: ✅ Track a leftTallest array & rightTallest array --> makes "inner loop of Naive solution" more efficient (reduces repeated work)
  - **Two Pointers**: ✅ Track leftTallest and rightTallest height --> saves us space

### Plan
General idea:  
- Create highest_left and highest_right
- While L < R:
  - if highest_left < highest_right --> water is limited by left side, track water, l--, update highest_left
  - else: water is limited by right side, track water, R--, update highest_right
- return res

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)   

---


