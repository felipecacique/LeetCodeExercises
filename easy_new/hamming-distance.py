class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # https://leetcode.com/problems/hamming-distance/
        
        xbin = list(reversed(bin(x)[2:]))
        ybin = list(reversed(bin(y)[2:]))
        count = 0
        if len(xbin)<len(ybin):
            xbin, ybin = ybin, xbin

        for i in range(len(xbin)):
            if i >= len(ybin):
                if xbin[i] == '1':
                    count += 1
                continue
            if xbin[i] != ybin[i]:
                count += 1
        return count