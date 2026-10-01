#input: array of integers representing daily temperatures on ith day
#output: array where [i] is the number of days after the ith day b4 a warmer temp appears on a future day
#questions: Would I return an empty array for an empty input array? Can temperatures be negative? What are the recommended complexities? I think we can get O(n) time complexity optimally and O(n) space complixity optimally
#straightforward solution: Left and right pointer at start of array, right pointer iterates until hits a number higher than left pointers. If so, note down number of right iterations and put into results array, then left iterates one, and right comes back to left pointer. Repeat until left reaches end of array.
#optimal solution: initialize empty stack and result array with 0 for len of input. go through input array: compare top of non-empty stack to number. if top is lesser: pop until stack is empty or top of stack is greater than current temperatur. Then, push current temperature onto stack a tuple (temp, index). popped items respective indices in result array should be updated based on current index - tuple index to track number of days passed. push tuple onto stack (temp, index) no matter what. Repeat until reach end of array. items still in stack will have 0 in result array. 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            if stack and stack[-1][0] < temperatures[i]:
                while stack and stack[-1][0] < temperatures[i]:
                    result[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
            stack.append((temperatures[i], i))
        return result
            


            
        