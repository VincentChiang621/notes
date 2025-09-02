# 121. Best Time to Buy and Sell Stock

🔗 **Link:** [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)  
💡 **Difficulty:** Easy

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - Can numbers in the array < 0?
  - How can I handle len(prices) <= 1?
  - What if the `prices` was a non-increasing array?
  - Do you HAVE to buy and sell? 

- Naive Solution:
  - Run a nested for loop and to checek EVERY buy/sell pair
  - O(n^2)

### Match
- Problem Type: **Sliding window**  
- Strategies:
  - **Sorting**: ❌ Not useful, since we need indicies to match sell after buy.
  - **Sliding Window**: ✅ Always track the minimum price so far, then update profit when higher prices found

### Plan
General idea:  
- Use L,R pointers and only update L when its value is bigger than R
- R just keeps running forward in a for loop


### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N)  
- **Space Complexity:** O(1)
  
---


