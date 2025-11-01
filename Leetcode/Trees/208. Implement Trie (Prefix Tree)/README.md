# 208. Implement Trie (Prefix Tree)

🔗 **Link:** [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)  
💡 **Difficulty:** Medium
---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can you insert an empty string?
  - What if you insert(“apples”) and search startsWith(“apples”)

### Match
- Problem Type: **Trees**  
- Strategies:
  - **Trees**: Node() hashmap: char -> next Node()

### Plan
General idea:  
- Each letter is a treenode()
- And each layer/level of the tree is each ith letter of the string
- If i would like to find “apples” after insertion, i would go down the tree level by level to find a,p,p,l,e,s


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


