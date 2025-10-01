class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        steps = []  # steps[i] = [pos[i], speed[i]]

        for i in range(len(position)):
            steps.append([position[i], speed[i]])

        steps.sort()    # sorted with 
        stack = []  # stores steps to target

        for i in range(len(steps)-1, -1, -1):
            cur = steps[i]
            speed = (target - cur[0]) / cur[1]
            stack.append(speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)