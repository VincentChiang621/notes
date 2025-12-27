# 684. Redundant Connection

🔗 **Link:** [Redundant Connection](https://leetcode.com/problems/redundant-connection/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - 

### Match
- Problem Type: **Graph**  
- Strategies:
  - **Graph**:  

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


