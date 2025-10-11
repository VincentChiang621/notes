# 981. Time Based Key-Value Store

🔗 **Link:** [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - What will happen if i set the same key, value, timestamp pair twice?
  - Can timestamp be negative?
  - If we want to use get(), what if the key isn’t in the data structure?
  - So basically, get() returns the largest timestamp_prev that is at most timestamp?
  - Can I have one key with different timestamps? If so, what should I return with get()?

### Match
- Problem Type: **Binary Search + Hashmap**  
- Strategies:
  - **Binary Search**: since increasing timestamp, get() can use binary search
  - **Hashmap**: Efficient for storing key value pairs, can use [] as a value and insert by timestamp

### Plan
General idea:  
- I want to use a hashmap to store the key, then store the [timestamp, val] pair in sorted order
- set() = O(1) because i will just append to the end since timestamp is always increasing
- get() = O(logn) with binary search since timestamp sorted

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** set() = O(1), get() = O(logn)
- **Space Complexity:** O(n)  

---


