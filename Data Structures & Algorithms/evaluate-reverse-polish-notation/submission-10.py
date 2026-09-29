#input: array of tokens representing a valid arithmetic expression
#output: integer representing evaluation of expression
#questions: what do we return if we divide by 0 somewhere in the expression? What sort of complexity are we looking for here, space and time wise? Should we always assume priority of first tokens as seen in the example?
#straightforward solution: loop through array until at end. If encounter number and prev empty: store as prev. If encounter number and prev is a number: store as curr. If encounter operation. perform operation on prev and curr. FAULTY
#optimal solution: go through array. If encounter integer, push onto stack. If encounter operator, pop top 2 items from stack and perform operation, then push back onto stack. repeat until end of array
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                if i == "+":
                    stack.append(stack.pop() + stack.pop())
                elif i == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif i == "*":
                    stack.append(stack.pop() * stack.pop())
                else:
                    a, b = stack.pop(), stack.pop()
                    stack.append(int(b / a))
        return stack[0]
