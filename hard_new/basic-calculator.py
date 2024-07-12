class Solution:
    def calculate(self, s: str) -> int:
        # https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
        chars = set(['+', '-', '(', ')'])
        nums = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        s = s.replace(" ", "")
        arr = []

        # String to array
        for c in s:
            if len(arr) > 0 and c.isdigit() and arr[-1].isdigit(): 
                arr[-1] += c
            else:
                arr.append(c)

        # Solving the problem using stack
        stack = []
        for c in arr:
            stack.append(c)
            flag = True
            while flag:
                flag = False
                # Lets solve the unary "-" by adding a zero on the left, or actually lets just make the sumber become negative
                if (len(stack) >= 3 and stack[-1] not in chars and stack[-2] == "-" and stack[-3] == "(") or (len(stack) ==2 and stack[-1] not in chars and stack[-2] == "-"):
                    value = stack.pop()
                    stack.pop()
                    stack.append(str(-1*+int(value)))
                    flag = True
                # Sum up the eqquation inside the parentesis
                elif len(stack) >= 3 and stack[-1] not in chars and stack[-2] in ["+", "-"] and stack[-3] not in chars:
                    value = 0
                    if stack[-2] == "+":
                        value = int(stack[-3]) + int(stack[-1])
                    elif stack[-2] == "-":
                        value = int(stack[-3]) - int(stack[-1])
                    stack.pop()
                    stack.pop()
                    stack.pop()
                    stack.append(str(value))
                    flag = True

                # Drop off the parentesis after the equation inside have been solved
                elif len(stack) >= 3 and stack[-1] == ")" and stack[-2] not in chars and stack[-3] == "(":
                    stack.pop()
                    value = stack.pop()
                    stack.pop()
                    stack.append(value)
                    flag = True

        return int(stack[0])