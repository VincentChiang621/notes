# 973. K Closest Points to Origin

🔗 **Link:** [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Clarify input/output: points: List[List[int]], k: int → List[List[int]]
  - Test case: points = [[0,0], [0,1],[0,2],[1,0]], k = 3 → [[0,0], [0,1],[1,0]]
  - Can inputs be null/empty? no
  - Can k > len(points)? no

- Naive Solution:
  - Sort this array based on a lambda function that takes into account the euclid distances
  - This would take O(nlogn) Time and O(n) Space


### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: efficient to pop from k top elements

### Plan
General idea:  
- initialize minheap with elements [dist, x, y]
- heapify
- pop from heap `k` times

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(klogn)  
- **Space Complexity:** O(n)  

---


