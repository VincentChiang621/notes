# 295. Find Median from Data Stream

🔗 **Link:** [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - What are the use cases of these functions, how often will we use add() compared to findMedian()?
    - we will be calling add() way more than findMedian()
  
- Naive (slow add, fast find()):
  - add(int) → None:
    - Keep a list of sorted ints, add using Binary search
    - Time: O(#elements) we need to shift elements of array
  - findMedian() → float:
    - O(1) just get the median element using index


### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: min and maxHeap

### Plan
General idea:  
- firstHalf = maxHeap and secHalf = minHeap
- we can maintain these two heaps and getMedian in O(1)
- median is just secHalf[0] or (secHalf[0] + firstHalf[0]) / 2

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(logN)  
- **Space Complexity:** O(N)  

---


