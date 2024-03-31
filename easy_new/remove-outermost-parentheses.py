class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # https://leetcode.com/problems/remove-outermost-parentheses/
        stack = []
        decomposition = ""
        decompositions = ""
        for c in s:
            decomposition += c
            stack.append(c)
            if len(stack) > 1:
                if stack[-1] == ")" and stack[-2] == "(":
                    stack.pop()
                    stack.pop()
            if len(stack) == 0:
                # just have a primitive decomposition
                decompositions += decomposition[1:-1]
                decomposition = ""
            
        return decompositions