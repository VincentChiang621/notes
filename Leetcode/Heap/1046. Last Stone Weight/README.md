# 1046. Last Stone Weight

🔗 **Link:** [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - what should be returned if no stones remain, [10,10] -> 0
  - input: List[int] -> output: int
  
- Naive Solution:
  - loop everytime and check for top two largest, then pop them
  - push the result
  - do this until 0 or 1 stone left
  - Time: O(n * #collision) 

### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: useful to get the top two stones in O(logn)

### Plan
General idea:  
- make a maxHeap of stones
- pop top 2 biggest
- smash then and add remainder stone if applicable
- return maxHeap[0] or 0

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(nlogn)  
- **Space Complexity:** O(n)  


---


