# 621. Task Scheduler

🔗 **Link:** [Task Scheduler](https://leetcode.com/problems/task-scheduler/description/)  
💡 **Difficulty:** Medium

---


## UMPIRE Method

### Understand
- Clarifying questions:
  - [A,B,C,D] , n = 10 → return 4
  - [A,A,A,A,A], n = 2 → return 10
  - [A,A,A,B,B,C,D], n = 3 → A,B,C,D,A,B,idle,idle,A
  - [A,A,A,B,B,C,D], n = 2 → A,B,C,A,B,D,A
  - [A,B,A,B,A,B], n = 2 → A,B,idle,A,B,idle,A,B


### Match
- Problem Type: **Heap**  
- Strategies:
  - **Heap**: for popping most frequent TASK

### Plan
General idea:  
- create frequency map
- use a maxHeap on frequencies, and keep a queue for tasks
- while we have things in maxHeap or queue
  - pop from the maxHeap (Greedy), put in queue if not done
  - pop from queue and push to maxHeap 
  - update time

### Implement
➡️ See `solution.py` for the full implementation.  

### Review
- Walk through examples to verify correctness.  
- Debug as if a bug exists to confirm logic holds.  

### Evaluate
- **Time Complexity:** O(N log26)  
- **Space Complexity:** O(N)  

---


