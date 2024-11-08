class Solution:
    def numberOfWays(self, s: str) -> int:
        # https://leetcode.com/problems/number-of-ways-to-select-buildings/?__cf_chl_tk=W5EGSoVwpNR.e8Lbr63G_XStC3DCPY8h71KLZO.wz4U-1731022423-1.0.1.1-DZASG56KN8Rc4V7ECfmeWox8tn91WGfsPC3bsoX3uCg
        # time O(n) space O(1)
        # using dp, with prefix sum. Complicadinho a logica.

        count1 = 0
        count0 = 0
        comb2Pairs0 = 0
        comb2Pairs1 = 0
        comb2Pairs0Total = 0
        comb2Pairs1Total = 0
        comb3Pairs0 = 0
        comb3Pairs1 = 0
        comb3Pairs0Total = 0
        comb3Pairs1Total = 0

        for c in s:
            if c == "1": 
                comb3Pairs1 = comb2Pairs0Total
                comb3Pairs1Total += comb3Pairs1

                comb2Pairs1 = count0
                comb2Pairs1Total += comb2Pairs1
                
                count1 += 1

            else: 
                comb3Pairs0 = comb2Pairs1Total
                comb3Pairs0Total += comb3Pairs0

                comb2Pairs0 = count1
                comb2Pairs0Total += comb2Pairs0
                count0 += 1

        return comb3Pairs1Total + comb3Pairs0Total
