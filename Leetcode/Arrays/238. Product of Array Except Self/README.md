# 238. Product of Array Except Self

🔗 **Link:** [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Could nums[i] be negative, zero, positive?
  - How many elements does nums typically have (general usecase)

  
- Naive Solution:
  - Initiate another array, same size as nums
  - Do a nested for loop to find out what all res[i] should be
  - Time: O(n^2) and Space: O(n)


### Match
- Problem Type: **Array + Prefix**  
- Strategies:
  - **Prefix**: ✅ product can be broken down into two parts, pre-product and post-product. Both only take O(n) 

### Plan
General idea:  
- Prefix, postfix sums
- Use two arrays, one for prefix one for postfix:

- Even better, just use pointer to track prefix/postfix.


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1) since output array doesn't count  

---


