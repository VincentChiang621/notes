# 143. Reorder List

🔗 **Link:** [Reorder List](https://www.youtube.com/watch?v=S5bfdUTrKLM)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can `head` be empty
  - are we creating new list nodes or just rearranging ptrs

### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: reverse linked list then arrange ptrs 

### Plan
General idea:  
- use slow and fast to get to the middle of LL
- reverse the second half (Starting from slow)
- update pointers

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O()  

---


