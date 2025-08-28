# 36. Valid Sudoku

🔗 **Link:** [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Are we guaranteed a non-empty 9x9 matrix (sudoku board)?
  - Are we guaranteed only '1'-'9' or '.' in any cell?

  
- Naive Solution:
  - Just do three checkers (loops): 1.rows, 2.cols, 3.sub-boxes
  - Use a hashset to track for repeating letters
  - Indexing correctly for 1, 2 is easy, but 3 might be more difficult


### Match
- Problem Type: **Array + Hashset**  
- Strategies:
  - **Hashset**: ✅ Efficient checking for duplicate elements
  - **Array**: ✅ Storing each hashmap in a different array

### Plan
General idea:  
- Each row has its own hashmap stored in an array of 9 rows
- Same for cols and subboxes.
- When going through each element check for duplicates for row, cols, and subboxes and add number to hashset

- Alternative: use hashmap (instead of array) and tuple(r//3, c//3) as the key for subboxes. 

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N^2) or O(1) since 9x9 sudoku is fixed
- **Space Complexity:** O(N^2) or O(1) since 9x9 sudoku is fixed

---


