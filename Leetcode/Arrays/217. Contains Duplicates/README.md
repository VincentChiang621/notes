# 217. Contains Duplicates

🔗 **Link:** [Contains Duplicates](https://leetcode.com/problems/contains-duplicate/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can the `nums` array be empty?
  - Is it reasonable to assume that `nums` only include integers (negatives, positives, zeros)?  
  - Is the array sorted?
  - Any requirement on time/space complexity?

- Naive Solution:
  - Run a nested for loop and check each element to see if match
  - Problem -> repeated work for checking... 

### Match
- Problem Type: **Array + Hashset**  
- Strategies:
  - **Sorting**: ✅ Useful, since duplicates will appear next to each other
  - **Hashset**: ✅ Efficient lookup and insert  

### Plan
General idea:  
- Create `seen` hashset that stores elements in nums
- iterate thru `num` and return whether each element is seen or not 

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


