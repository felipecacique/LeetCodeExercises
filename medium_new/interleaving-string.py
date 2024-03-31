class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # https://leetcode.com/problems/interleaving-string/?envType=study-plan-v2&envId=top-interview-150
        # O(mxn) we will build the paths that leads to s3, using s1 and s2 table format. We will fill the vertice with 1 if a path leads to it

        if len(s3) != len(s1) + len(s2): return False
        # if s3 == "": return True
        # if s2 == "":
        #     if s3 == s1: return True
        #     else: return False
        # if s1 == "":
        #     if s3 == s2: return True
        #     else: return False

        grid = [[0] * (len(s1)+1) for _ in range(len(s2)+1)] # we created an extra left column and top row, wich is the start state
        
        # the base case
        grid[0][0] = 1 

        # creating the path in the grid
        for j in range(0,len(s2)+1):
            for i in range(0,len(s1)+1):
                if i == 0 and j == 0:
                    continue
                # pathSize = i + j # qtd char in the sequence including grid[j][i]
                if j-1 >= 0 and grid[j-1][i] == 1: # moving down
                    if s3[i+j-1] == s2[j-1]: # we can only add the s2 if we are moving down
                        grid[j][i] = 1
                if i-1 >= 0 and grid[j][i-1] == 1: # moving to the right
                    if s3[i+j-1] == s1[i-1]:
                        grid[j][i] = 1

        return grid[-1][-1]