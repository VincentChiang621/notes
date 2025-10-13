# 21. Merge Two Sorted Lists

🔗 **Link:** [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - can `list1` and `list2` be empty -> yes
  - are `list1` and `list2` guarenteed to be sorted -> yes

### Match
- Problem Type: **Linked Lists**  
- Strategies:
  - **Linked Lists**: pointer arrangement

### Plan
General idea:  
- keep a dummy node in front
- compare `list1.val` and `list2.val` and attach dummy.next to the smaller one
- update ptrs

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)  

---


