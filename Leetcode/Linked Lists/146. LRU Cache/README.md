# 146. LRU Cache

🔗 **Link:** [LRU Cache](https://leetcode.com/problems/lru-cache/description/)  
💡 **Difficulty:** Medium
---


## UMPIRE Method

### Understand
- Clarifying questions:
  - From the question, we remove the least recently used, how do we define that? 
  - Can i assume put() or get() uses the cache? -> yes

  
- Naive Solution:
  - Create a member variable (hashmap) that tracks our key, values for efficient lookups
  - Use a list to track the LRU keys
  - Update the list whenever you get or put, may take up to O(n) time because updates the whole list (shifting LRU elements) 


### Match
- Problem Type: **Hashmap + Linked Lists**  
- Strategies:
  - **Linked Lists**: add and removes nodes with O(1), can be used to add (to MRU) and remove (from LRU)
  - **Hashmap**: underlying cache, stores the key, value pairs efficiently

### Plan
General idea:  
- hashmap stores key -> Node()
- Node stores key, val, nextptr, prevptr
- Dummy Nodes: MRU and LRU
- Helpers: removeNode, addNode (self explanatory)
- put(key, val):
  - if full and new key == overflow
    - removeLRU
    - make new node, add to MRU
  - elif key in cache: 
    - remove()
    - add()
  - else:
    - add()

- get(key):
  - if not in cache: return -1
  - remove()
  - add()


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** avg O(1)  
- **Space Complexity:** O(N)  

---


