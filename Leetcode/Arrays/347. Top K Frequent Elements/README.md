# 347. Top K Frequent Elements

🔗 **Link:** [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)  
💡 **Difficulty:** Medium  

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Input: nums: List[int], k: int → List[int]
  - Can `nums` be empty and can `k` <= 0?
  - Is nums sorted?
  - How do we break ties?
  - Can k > # unique nums
  - nums = [1,2,6,4,4,1], k = 2 → [1,4]
  - nums = [5,5,5,5,5], k = 1 → [5]
  - nums = [1,2,3,4], k = 4 → [1,2,3,4]

  
- Naive Solution:
  - Use a hashmap that stores nums -> frequency
  - Sort the frequencies from descending order O(nlogn)
  - Pop top numbers from the hashmap
  - NOT better than O(nlogn) -> need another solution


### Match
- Problem Type: **Array + Hashmap + Heap**  
- Strategies:
  - **Heap**: ✅ Useful, since we only need TOP K frequent element
  - **Hashmap**: ✅ Efficient for storing values with frequency
  - **Bucket Sort**:  ✅ Great since frequency is bounded by `len(nums)`

### Plan
General idea:  
- Count frequency of all elements with hashmap O(n)
- Fill bucket, frequency -> list of elements (with that freq) 
- Extract the k-frequent going from the back of buckets array

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(N)  

---


