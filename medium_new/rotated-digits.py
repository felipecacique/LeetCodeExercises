class Solution:
    def rotatedDigits(self, n: int) -> int:
        # https://leetcode.com/problems/rotated-digits/
        # if at least one of the digits are 2, 5, 6 or 9, then x is good
        
        count = 0
        valid = set(['2','5','6','9'])
        not_valid = set(['3','4','7'])
        for i in range(1,n+1):
            string = str(i)
            flag = True
            for s_ in string:
                if s_ in not_valid:
                    flag = False
                    break
            if flag:
                for s in string:
                    if s in valid:
                        count += 1
                        break
        
        return count