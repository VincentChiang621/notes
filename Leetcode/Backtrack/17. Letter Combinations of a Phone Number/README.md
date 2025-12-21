# 17. Letter Combinations of a Phone Number

🔗 **Link:** [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - does the ordering of digits matter -> yes

### Match
- Problem Type: **Backtrack**  
- Strategies:
  - **Backtrack**: brute force all letter combinations

### Plan
General idea:  
- Create a hashmap to map '2': 'abc', '3': 'def', etc
- dfs(ind):
- base case: if ind == len(digits): append to res
- branch out to ALL in that letter


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(4^N)  
- **Space Complexity:** O(N)   

---



