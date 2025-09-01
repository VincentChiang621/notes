# 11. Container With Most Water

🔗 **Link:** [Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Are elements in height guaranteed to be positive?
  - Can height be an empty array?
  - So a container can only hold up to min(height[i], height[j]) * j - i water?
  - What are the usecases of this function? Do we need to implement for efficiency in case of large `height` arrays?

  
- Naive Solution:
  - Run a nested for loop to check every combination of areas
  - O(n^2)

### Match
- Problem Type: **Array + Two Pointers**  
- Strategies:
  - **Two Pointers**: ✅ start from both ends, increment/decrement the smaller height to look for bigger area

### Plan
General idea:  
- Realization: starting from both ends, we can check for maximizing easier because we just move the pointer that is hindering our container size forward.
- Start with two pointers on each end
- Use a greedy approach and move the ptr of shorter line forward


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


