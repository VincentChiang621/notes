# 271. Encode and Decode Strings

🔗 **Link:** [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Two functions: encode(List[str]) → str | decode(str) → List[str]
  - What types of characters are included in the strings?
  - What are the general use cases of these functions? Will they be called a lot on bigger inputs, if so what are the time complexity targets (or would you like me to figure that myself)? 
  - How do we handle empty strings in the list?
  - [‘hello’, ‘’, ‘world’]
  - Edge cases: [‘’, ‘’, ‘’, ‘’], []

  
- Naive Solution:
  - Use a separator like “#” or “|” to separate between words
  - problem: [“#”, “”] → “##” [“##”] → “##”
  - Doesn’t work because of tricky string characters that might mess up our decode


### Match
- Problem Type: **String + Array**  
- Strategies:
  - **String Manipulation**: ✅ Format: "<len(strs[i])>#<strs[i]" 

### Plan
Encode:  
- Append length, delimiter BEFORE actual string
- [‘hello’, ‘’, ‘world’] → “5#hello0#5#world”
- [“#”, “”] → “1##0#”
- [“##”] → “2###”

Decode:
- Grab (length)integer before delimiter “#”
- String is guaranteed to be length after #.


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


