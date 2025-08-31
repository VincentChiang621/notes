# 167. Two Sum II

🔗 **Link:** [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - What is the general use case for this function? Do we need to worry about very large inputs?
  - Can there be duplicates in `numbers`
  
- Naive Solution:
  - see 1. Two Sum

### Match
- Problem Type: **Two Pointers**  
- Strategies:
  - **Two Pointers**: O(n), efficient for this problem

### Plan
General idea:  
- Set our l,r pointers at two opposite ends of `numbers`
- If we numbers[l] + numbers[r] > tar: we need smaller sum, so r -= 1
- Else: l += 1 since we are guaranteed an answer


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1) l,r pointers are constant space  

---


