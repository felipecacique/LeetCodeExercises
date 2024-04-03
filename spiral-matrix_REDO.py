class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        m = [[-1] * n for _ in range(n)]
        k = 1
        i = 0
        j = 0
        while k <= n*n:

            # moving right
            while i < n+1:
                if i >= n or m[j][i] != -1:
                    i -= 1
                    j += 1
                    break
                m[j][i] = k
                k += 1
                i += 1
                
            # moving down    
            while j < n+1:
                print("bla")
                if  j >= n or m[j][i] != -1:
                    j -= 1
                    i -= 1
                    break
                m[j][i] = k
                k += 1
                j += 1
                
            # moving left    
            while i >= 0-1:
                if i < 0 or m[j][i] != -1:
                    i += 1
                    j-=1
                    break
                m[j][i] = k
                k += 1
                i -= 1
                
            # moving up    
            while j >= 0-1:
                if j < 0 or m[j][i] != -1:
                    j += 1
                    i += 1
                    break
                m[j][i] = k
                k += 1
                j -= 1
                    
        return m
    
    
#             for i in range(start_right, end_right):
#                 m[b][i], k, = k, k+1
#                 # start_right = start_right + 1
#                 end_right = end_right - 1
         
#             for j in range(start_bottom, end_bottom):
#                 m[j][i], k, = k, k+1
#                 # start_bottom = start_bottom + 1
#                 end_bottom = end_bottom - 1
         
#             for i in range(start_right, end_right):
#                 m[b][i], k, = k, k+1
#                 start_right = start_right + 1
#                 end_right = end_right - 1