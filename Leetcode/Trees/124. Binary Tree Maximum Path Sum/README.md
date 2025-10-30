# 124. Binary Tree Maximum Path Sum

🔗 **Link:** [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)  
💡 **Difficulty:** Hard

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - So a path may extend from one node to another node, doesn’t have to go through root? yes

- Naive Solution:
  - Check the path and record the sum for each node
  - Time: O(2^n)

### Match
- Problem Type: **Binary Trees**  
- Strategies:
  - **Binary Trees**: use DFS and return node.val or node+left or node+right

### Plan
General idea:  
- The max path sum of a node is just 
    - Take right only
    - Take left only
    - Take only itself
    - Take both left and right
      - but we cant return this (only track)

Track the maxSum of every node


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


