# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        # lets add the brackets one by one into a stack (LIFO), and at each push we check if the last 2 char correspond to an open and closed bracked. If so, we remove them form the stack. We keep doing this until we have push all chars. If the stack is empty, it means that we all open brackets have found its equivalent close bracket, and then the string is valid.

        def Solution1():
            # implementation of a stack using a list
            stack = []

            if len(s) <= 1:
                return False

            for i, c in enumerate(s):
                stack.append(c)
                if len(stack) > 1 and stack[-2] + stack[-1] in ["()", "{}", "[]"]:
                    stack.pop()
                    stack.pop()

            if stack == []:  # stack is empty
                return True
            else:
                return False

        return Solution1()
