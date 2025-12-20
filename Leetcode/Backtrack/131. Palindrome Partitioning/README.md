# 131. Palindrome Partitioning

🔗 **Link:** [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can we have duplicate substrings? [aa,b,b,a,a] and [a,a,b,b,aa] -> yes

### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: brute force results, stop looking when we dont have palindrome

### Plan
General idea:  
- []: to keep track of potential palindrome subarrays
- ind: starting index
- if palindrome, add to potential subarrays
- base case: if ind == len(s)

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N*2^N)  
- **Space Complexity:** O(N)  

---



