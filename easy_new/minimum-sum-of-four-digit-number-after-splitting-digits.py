class Solution:
    def minimumSum(self, num: int) -> int:
        # https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/
        digits = [0] * 4
        for i in range(4):
            digits[i] = num%10
            num = num//10
        
        c = [[]]
        for _ in range(4):
            newCom = []
            for com in c[:]: 
                for i in range(4):
                    if not i in com:
                        d = com + [i]
                        newCom.append(d)
            c = newCom

        pairsSum = []
        for i, j, k, l in c:
            pairsSum.append(digits[i]*10+digits[j] + digits[k]*10+digits[l])
            pairsSum.append(digits[i]*100+digits[j]*10+digits[k] + digits[l])
            
        return min(pairsSum)
        