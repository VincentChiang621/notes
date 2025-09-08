# 424. Longest Repeating Character Replacement

🔗 **Link:** [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Are characters in s limited to upper case English characters?  
  - Can s be empty?
  - What are the range of numbers for integer k 
  
- Naive Solution:
  - Checked all substrings
  - Get first char
    - Check if next chars match:
    - If not, decrease k and continue
    - If match, keep going
  - Return length of max longest
  - O(N^2) time with O(1) space


### Match
- Problem Type: **Array + Hashmap + Sliding Window**  
- Strategies:
  - **Sliding Window**: ✅  Useful, window tracks charMap, check if window can be k-replaced, if not, move l forward  
  - **Hashmap**: ✅ Efficient for storing a char -> frequency map  

### Plan
General idea:  
- Sliding window of L,R. Tracks charCounts between s[l] to s[r]
- k-replaceable: (r - l + 1) - max_f <= k
- if k-replaceable:
  - update res
- else: 
  - keep moving l_ptr and update charCounts

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


