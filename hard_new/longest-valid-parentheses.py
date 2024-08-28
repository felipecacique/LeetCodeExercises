class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # https://leetcode.com/problems/longest-valid-parentheses/description/?envType=study-plan-v2&envId=top-100-liked
        # o(n) o(n)

        indexesValid = set() # get the indexes of the valid parentesis
        stack = []
        for i, char in enumerate(s):

            stack.append((char,i))

            if len(stack) >= 2 and stack[-1][0] == ")" and stack[-2][0] == "(":
                _, i1 = stack.pop()
                _, i2 = stack.pop()
                indexesValid.add(i1)
                indexesValid.add(i2)
        
        cumSum = 0
        maxCumSum = 0
        for idx in range(len(s)):
            cumSum += 1
            if idx not in indexesValid:
                cumSum = 0
            maxCumSum = max(maxCumSum, cumSum)
        
        return maxCumSum







# someone's soltion
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         st=[-1]
#         ans=0
#         for i in range(len(s)):
#             if s[i]==')' and len(st)>1 and s[st[-1]]=='(':
#                 st.pop(-1)
#                 ans=max(ans,i-st[-1])
#             else:
#                 st.append(i)
                
#         return ans