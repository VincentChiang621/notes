# 1448. Count Good Nodes in Binary Tree

🔗 **Link:** [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - if node X is equal to the largest val in its path to root, is it "good"? -> yes (greater or equal than)
  - can root be null? -> no
  
### Match
- Problem Type: **Binary Trees**  
- Strategies:
  - **Binary Trees**: use DFS (post traversal) to track "good nodes" = left + right + 1 (depending on circumstance)

### Plan
General idea:  
- base case: if root == None: return 0
- if maxVal <= root.val:
  - return l + r + 1
- else:
  - return l + r

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(H)  

---


