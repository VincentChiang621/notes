# 1. Two Sum

🔗 **Link:** [Two Sum](https://link.com)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can the `nums` array be empty?  
  - Any requirement on time/space complexity?  
  - Is the array sorted?  
  - Will the numbers in the array duplicate?  
  
- Naive Solution:
  - Run a nested for loop and check each element to see if match
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


