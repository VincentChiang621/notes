# 128. Longest Consecutive Sequence

🔗 **Link:** [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - I’m assuming consecutive elements means something like 1,2,3, can it span to negatives like -1,0,1,2,3,4?
  - Are duplicates allowed in nums?
  - Can nums be empty?
  - Nums = [] → 0
  - Nums = [0,-1,2,4,6,5] → 3
  - Nums = [9,7,8,5,6,] → 5
  
  
- Naive Solution:
  - Sort nums and check for consecutive integers with a for loop

### Match
- Problem Type: **Array + Hashset**  
- Strategies:
  - **Hashset**: ✅ ONLY store the first (smallest) element of each starting consecutive sequence using a hashset. Then forloop for each sequence to check for the length


### Plan
General idea:  
- Create a hashset and convert `nums` into a set.
- Only do this sequence check if `nums[i] - 1` is not in hashset

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  
- Notes1: Looks like a nested loop BUT only enter the while loop if it is the start of a sequence
- Notes2: Each number in the set `nums` is only part of one sequence, so each element is only visited once!

---


