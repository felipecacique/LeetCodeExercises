class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
      # https://leetcode.com/problems/edit-distance/?envType=study-plan-v2&envId=leetcode-75
      # solution O(mxn)
      # https://www.youtube.com/watch?v=HwDXH35lr0o&list=FLuLnbXnMa2w0iSGACDOkJDw&index=1&ab_channel=NikhilLohia

        minDists = [[0] * (len(word1)+1) for _ in range(len(word2)+1)] # it will stores our minDistances

        # initialize matrix
        for i in range(len(word2)+1): minDists[i][0] = i
        for i in range(len(word1)+1): minDists[0][i] = i
        
        # populate matrix
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word2[i] == word1[j]:
                    minDists[i+1][j+1] = minDists[i][j]
                else:
                    minDists[i+1][j+1] = min(minDists[i][j], minDists[i+1][j], minDists[i][j+1]) + 1

        return minDists[-1][-1]

