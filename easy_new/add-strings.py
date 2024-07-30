class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # https://leetcode.com/problems/add-strings/
        revNum1 = num1[::-1]
        revNum2 = num2[::-1]
        n = max(len(num1), len(num2))
        
        output = ""
        leading1 = 0
        for i in range(n):
            n1 = int(revNum1[i]) if i < len(revNum1) else 0
            n2 = int(revNum2[i]) if i < len(revNum2) else 0
            n3 = (n1+n2+leading1) % 10
            leading1 = (n1+n2+leading1) // 10
            output += str(n3)
        if leading1 == 1: output += "1" 
            
        return output[::-1]
            