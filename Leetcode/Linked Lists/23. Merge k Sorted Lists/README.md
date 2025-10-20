# 23. Merge k Sorted Lists

🔗 **Link:** [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Should we create new nodes and return the head of the new Linked List or just rearrange pointers from the inputs?
  - Can `lists` have None pointers? -> yes
  
- Naive Solution:
  - Can we just merge the lists one by one?
  - As an example, merge lists[0], with lists[1], then merge that result with list[2] …
  - Then we get Time: O(n * k) = O(totalNodes * len(lists))


### Match
- Problem Type: **Heap + Linked Lists**  
- Strategies:
  - **Heap**: can find smallest in O(logk) time (minHeap)
  - **Linked Lists**: ptr movements

### Plan
General idea:  
- create heap (arr) with [values, ind, nodeAddress]
- we need ind to break ties
- keep updating our cur.next nodes from poping off minHeap
- add to minHeap if there is next node

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(Nlogk)  
- **Space Complexity:** O(k)  

---


