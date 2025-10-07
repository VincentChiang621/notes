# 875. Koko Eating Bananas

🔗 **Link:** [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can piles be empty?
  - Can h == 0
  - Can i have a testcase piles = [1,2,3,4], with h = 1? Does this mean h >= n

  
- Naive Solution:
  - Check all integers k starting with 1 to max(piles) one by one
  - For each k:
    - Checks if this k is valid for koko to finish in h hours
  - Time: O(k*n)


### Match
- Problem Type: **Binary Search**  
- Strategies:
  - **Binary Search**: Use binary search on `k` because it would make h non-decreasing relationship

### Plan
General idea:  
- Use binary search on the k to reduce k checks to logk
- O(logk*n)


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(n * log(max(piles)))
- **Space Complexity:** O(1)  

---


