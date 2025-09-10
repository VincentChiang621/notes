# 567. Permutation in String

🔗 **Link:** [Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)
💡 **Difficulty:** Medium 

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can s1 or s2 be empty?
  - Can len(s1) > len(s1)
  - Permutation in this case just means anagram?
 
  
- Naive Solution:
  - Simply asking if the charCounts of s1 matches any substring of s2
  - Keep a charCount of s1, then run a nested loop to get charMaps of all substrings of s2, check if matching
  - Time: O(len(s1) * len(s2)), Space:O(n)


### Match
- Problem Type: **Slding Window + Hashmap**  
- Strategies:
  - **Sliding Window**: ✅ Useful, check only substrings of size len(s1) inside s2
  - **Hashmap**: ✅ Efficient to comparing anagrams 

### Plan
General idea:  
- Create Array to store charCount for both s1, s2  
- initialize matches == (s1, s2 char matches)
- forloop starting len(s1) to len(s2)
  - check if matches == 26, returns true
  - updates matches when adding s[r]
  - updates matches when decreasing s[l]

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


