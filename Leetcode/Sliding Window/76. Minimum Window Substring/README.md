# 76. Minimum Window Substring

🔗 **Link:** [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Are there character restrictions on s and t?
  - Can len(t) > len(s)?

- Naive Solution:
  - Run a nested for loop and keep a counter for s and t
  - check the whole counter inside s and t to see if matches
  - O(len(s) * len(t) * 52) | Space O(52)

### Match
- Problem Type: **Hashmap + Sliding Window**  
- Strategies:
  - **Sliding Window**: ✅ Useful, we can just track the charCounts from [L,R]
  - **Hashmap**: ✅ Efficient storing charCounts and lookups

### Plan
General idea:  
- First track tCounts of `t` in a hashmap
- Using sliding window to keep track of how many characters are in [L,R]
- matches = 0, required = len(tCount)
- If matches < required>:
	- Keep appending to sCounts because we do not match
- While matches == required:
	- Tracks res as the length of [L,R]
	- Take away sCounts[L]
	- L += 1


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(len(s))  
- **Space Complexity:** O(1)  

---


