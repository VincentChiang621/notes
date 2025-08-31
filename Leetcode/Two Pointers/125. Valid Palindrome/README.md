# 125. Valid Palindrome

🔗 **Link:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can `s` be empty?
  - What types of characters are in `s`?
  
- Naive Solution:
  - filter out all non-alphanumeric and checking s == s[::-1]
  - O(n) space because we make a copy of the string

### Match
- Problem Type: **Array + Two Pointers**  
- Strategies:
  - **Two Pointers**: ✅ Efficient since we want to compare chars from both ends

### Plan
General idea:  
- create pointers l,r that point to two ends of `s`
- update l if s[l] not alphanumeric, same for r
- compare if s[l].lower() == s[r].lower()

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


