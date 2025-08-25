# 242. Valid Anagram

🔗 **Link:** [Valid Anagram](https://leetcode.com/problems/valid-anagram/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - What is the range of characters of strings `s` and `t`?
  - Can `s` and/or `t` be empty?  
  - Correct me if I'm wrong, the input is s:str, t:str and output is bool?  
  
- Naive Solution:
  - n/a

### Match
- Problem Type: **Array + Hashmap**  
- Strategies:
  - **Sorting**: ✅ Useful, sort both `s` and `t` and compare the strings.
  - **Hashmap**: ✅ Efficient for storing chars along with frequency.  

### Plan
General idea:  
- Hashmap that maps str character to frequency.  
- Iterate s to fill hashmap, iterate t to fill another hashmap.
- Compare two hashmaps frequencies.

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


