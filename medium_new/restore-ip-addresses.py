class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # https://leetcode.com/problems/restore-ip-addresses/submissions/1501296592/?envType=problem-list-v2&envId=backtracking
        
        dots = [[0]]
        
        for j in range(3):
            newDots = []
            for dot in dots:
                for i in range(1, len(s)):
                    
                    # skip if value > 255 or leading 0s
                    if j == 0 and s[:i] and (int(s[:i]) > 255 or (len(s[:i])>1 and s[:i][0]=='0')): continue
                    if j > 0 and s[dot[-1]:i] and (int(s[dot[-1]:i]) > 255 or (len(s[dot[-1]:i])>1 and s[dot[-1]:i][0]=='0')): continue
                    if j == 2 and s[i:] and (int(s[i:]) > 255 or (len(s[i:])>1 and s[i:][0]=='0')): continue

                    if i > dot[-1]:
                        aux = dot[:]
                        aux.append(i)
                        newDots.append(aux)       
                dots = newDots 
        
        print(dots)
        sol = []
        for _, dot1, dot2, dot3 in dots:
            sol.append( s[:dot1]+"."+s[dot1:dot2]+"."+s[dot2:dot3]+"."+s[dot3:] )

        return sol