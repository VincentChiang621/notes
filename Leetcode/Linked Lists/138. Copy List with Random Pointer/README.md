# 138. Copy List with Random Pointer

🔗 **Link:** [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/description/)  
💡 **Difficulty:** Medium
---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can node.random point to itself?
  - Can node.random produce cycles?
  - Can the input be empty?

- Naive Solution:
  - Create the nodes as we iterate through head
  - Problems: random could not be created yet, so how can we connect it?


### Match
- Problem Type: **Linked Lists + Hashmap**  
- Strategies:
  - **Linked Lists**: creating LL and updating pointers
  - **Hashmap**: Efficient to storing the pointer addresses of old nodes

### Plan
General idea:  
- nodeMap = {} # maps old address -> new address
- 1st pass = creates deep copies of nodes and put mappings in nodeMap
- 2nd pass = connect the random and next pointers 

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


