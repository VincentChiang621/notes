# 355. Design Twitter

🔗 **Link:** [Design Twitter](https://leetcode.com/problems/design-twitter/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can a user unfollow itself to not see its own posts? no

### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: use heap with timestamp

### Plan
General idea:  
- use counter for every postTweet
- use that counter to make minHeap
- pop top 10 

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(k=tweets followed)  
- **Space Complexity:** O(N) 

---


