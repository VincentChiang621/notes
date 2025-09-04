# 3. Longest Substring Without Repeating Characters

🔗 **Link:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can `s` be an empty string?
  - What characters are allowed in `s`?
  - What does substring mean?
  - Test Cases
    - s = “”
    - s = “abcdefg”
    - s = “abccbad”
    - s = “abcdefdbc”

  
- Naive Solution:
  - Use a nested for loop to check every single substring in `s`
  - Keep a set to check for duplicates 
  - Time: O(n^2) | Space: O(n)


### Match
- Problem Type: **Sliding Window + Hashset**  
- Strategies:
  - **Sliding Window**: ✅ Since we only care about continous sequence (substring), a sliding window can represent that  
  - **Hashset**: ✅ Efficiently store and check for duplicates, maintain a correct hashset of the current window

### Plan
General idea:  
- Use a set() to track duplicate characters
- Two pointer/sliding window where l, r tracks the start,end indices of characters in this substring
- maintain the set() so that it tracks the correct characters in a given l,r sliding window
- get the length by using len(set())


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  
- Notes: although it looks like a nested loop in the code, but the l and r pointers only move across the array once, only moving forwared
- this means that basically, each character is added to set once and deleted once (at most), giving O(N)

---


