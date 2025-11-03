# 211. Design Add and Search Words Data Structure

🔗 **Link:** [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Test case proposal: WordDictionary contains words(“one”, “two”, “ona”, “twe”, “three”)
  - search(“..e”) -> true
  - search(“twa”) -> false
  - search(“f..”) -> false
  - search(“t.r.e”) -> true
  - are there constraints on input size and expected time/space complexities?



### Match
- Problem Type: **Tries**  
- Strategies:
  - **Tries**: Useful as each level can help reduce much complexities. 

### Plan
General idea:  
- each node is a char of the word
- "cat" would be stored as c -> a -> t
- the search() would be going down the tree
  - if we have a '.':
      - look at ALL children (only one needs to return True)
  - else:
      - go down the tree and return false if necessary

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


