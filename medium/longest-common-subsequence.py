class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #pisemol  edgitolenaf  iol
        def SolutionBruteForce():
            dp = [[0] * len(text2) for _ in range(len(text1))] # stores the loggenst commom sequence so far

            longest = 0
            for k in range(len(text1)):
                size = 0
                pointer = 0
                dp = [[0] * len(text2) for _ in range(len(text1))] # stores the loggenst commom sequence so far
                for i in range(k,len(text1)):
                    for j in range(pointer,len(text2)):
                        if text1[i] == text2[j]:
                            size += 1
                            dp[i][j] += size
                            pointer = j + 1
                            break
                for x in dp: 
                    for a in x: 
                        longest = max(a,longest)

            return longest

        def SolutionDinamicProgramming():
            # https://leetcode.com/problems/longest-common-subsequence/?envType=study-plan-v2&envId=leetcode-75
            # solution: https://www.youtube.com/watch?v=e9tUPwZZSBI&ab_channel=NikhilLohia
            # https://www.youtube.com/watch?v=Ua0GhsJSlWM&ab_channel=NeetCode
            # O(m*n)

            dp = [ [0] * (len(text1)+1) for _ in range(len(text2)+1) ] # stores the loggenst commom sequence so far
            for i in range(1,len(text1)+1):
                for j in range(1,len(text2)+1):
                    if text1[i-1] == text2[j-1]:
                        dp[j][i] = dp[j-1][i-1]+1
                    else:
                        dp[j][i] = max(dp[j-1][i], dp[j][i-1])
            return dp[len(text2)][len(text1)]

        return SolutionDinamicProgramming()

         