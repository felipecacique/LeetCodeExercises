class Solution:
    def decodeString(self, s: str) -> str:
        # https://leetcode.com/problems/decode-string/submissions/1361765062/?envType=study-plan-v2&envId=leetcode-75
        # O(sol.size()) if worked with stringd addition properly (usinh "".join instead of a += char)
        s = list(s)
        stack = []
        for c in s:
            
            stack.append(c)
            if stack[-1] == "]":
                stack.pop()
                string = ""
                while stack[-1] != "[":
                    string += stack.pop()
                string = list(reversed(string))
                stack.pop()
                coef = 1
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                if number is not "": coef = int(number)
                
                string = coef*string

                for x in string:
                    stack.append(x)

        return "".join(stack)