# 49. Group Anagrams

🔗 **Link:** [Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Input: List[str], output: List[List[str]]?
  - Can strings be empty? Should they still be grouped?
  - Is it okay to return the result in any order, or should I preserve input order?
  - test case: [apple, apo, poa, appel, opp] -> [[apple, appel], [apo, poa], [opp]]
  
- Naive Solution:
  - Use a hashmap to map sorted string to resulting string | hashmap[‘aelpp’] = [‘apple’]
  - Fill the whole hashmap and return all lists
  - S = avglen(strs)
  - We need to sort ALL strs, so O(n * Slog(S))
 

### Match
- Problem Type: **Array + Hashmap**  
- Strategies:
  - **Sorting**: ✅ Useful, but we need to spend extra time + memory to sort every `strs[i]`
  - **Hashmap**: ✅ Efficient for tuples() as charCounts -> list of corresponding anagrams 

### Plan
General idea:  
- We don’t need to sort every string because we can use charMap as a key to hashmap
- Since s[i] only contains lowercase letters, i can count ‘abc’ as (1,1,1,0,...,0) and ‘cab’ would be the same tuple
- Cut back on sorting time. 


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N * S)  
- **Space Complexity:** O(N)  

---


