# 703. Kth Largest Element in a Stream

🔗 **Link:** [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)  
💡 **Difficulty:** Easy  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can len(nums) < k? -> yes
  - Is nums sorted? -> no

- Naive Solution:
  - __init__: store nums as a sorted array member variable O(nlogn)
  - add(): find index to add the `val` then shift whole array O(n)

### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: efficient to find top k elements

### Plan
General idea:  
- __init__(): make a minHeap of `self.k` elements
- add(): push val and pop val
- edge cases: when self.k > len(nums) -> not dont pop()

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(NlogN)  
- **Space Complexity:** O(logN)  


---


