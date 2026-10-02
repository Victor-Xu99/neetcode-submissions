#input: 2 arrays representing position and speed of n cars, target (destination in miles)
#output: integer representing number of car groups reaching target at same time
#note: cars can never pass each other
#questions: can the starting positions be non-unique? how are we supposed to track what cars become fleets? what complexities are we looking for here?
#straightforward solution: Repeatedly mutate positions array of cars' based on respective speeds until original input array is empty. For each iteration, we add the speed, and then we check if any of the cars' positions has exceeded any of the other cars' positions. If so, put those cars together into a fleet which will have speed of slower car. Once a fleet reaches the target, it will be removed from the array, and 1 will be added to the result.
#optimal solution: intialize new array with tuples of (position, speed). Sort by position. where 0th index is lesser position. go through this array from last to first. For each item in this array, push onto stack. compare pushed item to other adjacent item in stack. If the time it takes for the item already in the stack to reach the target is shorter or equal to the one that is being pushed onto the stack, pop the top item. Repeat until end of array. Return length of stack.
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for i in range(len(position)):
            combined.append((position[i], speed[i]))
        stack = []
        for p, s in sorted(combined)[::-1]: # Reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
        