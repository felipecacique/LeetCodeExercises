# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we iterate the list, when finding the first operator in i, se solve it by applaying it to the elements i-1 and i-2 (they will be numbers). Then we remove i, i-1 and i-3, and replace it with the solution of the operator. We could do it with a stack. Add char there, when we find an operator, we pop the 2 values on the top of the stack, calculate the operation and add the solution to the stack. Time O(n)

        stack = []
        for char in tokens:
            if char in ["+", "-", "*", "/"]:
                if len(stack) >= 2:
                    solution = 0
                    if char == "+":
                        solution = int(stack.pop()) + int(stack.pop())
                    elif char == "-":
                        num2 = int(stack.pop())
                        num1 = int(stack.pop())
                        solution = num1 - num2
                    elif char == "*":
                        solution = int(stack.pop()) * int(stack.pop())
                    elif char == "/":
                        num2 = int(stack.pop())
                        num1 = int(stack.pop())
                        solution = int(num1 / num2)
                    stack.append(solution)
            else:
                stack.append(char)

        return int(stack[-1])
