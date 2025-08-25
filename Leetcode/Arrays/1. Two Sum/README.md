# 1. Two Sum

🔗 **Link:** [Two Sum](https://leetcode.com/problems/two-sum/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can the `nums` array be empty?  
  - Is `nums` sorted?  
  - Can there be multiple answers? 
  - inputs(nums: List[int], target: int) -> outputs(List[int])?
  
- Naive Solution:
  - Nested for loop to go through every two number combinations to check if they add to target
  - Problem -> repeated work for checking... 

### Match
- Problem Type: **Array + Hashmap**  
- Strategies:
  - **Sorting**: ❌ Not useful, since we need to return indices.  
  - **Hashmap**: ✅ Efficient for storing values with indices and checking complements quickly.  

### Plan
General idea:  
- Create a hashmap to store each number and its index.  
- For each element, check if its complement (`target - num`) exists in the hashmap.  
- If found, return the indices.  
- Otherwise, store the current number and index in the hashmap.  

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  
- ✅ Pros: Fast lookup with hashmap.  
- ❌ Cons: Extra memory usage.  

---


