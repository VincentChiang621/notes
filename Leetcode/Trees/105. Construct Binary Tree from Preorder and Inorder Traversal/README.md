# 105. Construct Binary Tree from Preorder and Inorder Traversal

🔗 **Link:** [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Is my goal to create this binary tree and return the root? yes
  - Are we guaranteed the preorder and inorder to be correct? yes 
  - Can it be empty? no

### Match
- Problem Type: **Binary Trees**  
- Strategies:
  - **Binary Trees**: DFS

### Plan
General idea:  
- element = preorder[0] will always be root.val
- Inorder[element] we can find out who is in left and right child
- 1. build root: root = TreeNode(preorder[0])
- 1b. ind = inorder.index(preorder[0])
- 2. root.left = dfs(inorder[:ind])
- 3. root.right = dfs(inorder[ind+1:])
- 4. return root

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  
---


