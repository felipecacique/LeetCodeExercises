# https://leetcode.com/problems/word-search/description/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # graph search, dfs, starting from each node, trying to complete the word. 
        
        def Solution1(board, word):
            # lets do it iteravively

            m = len(board)
            n = len(board[0])
            p = len(word)

            
            for i_start in range(0,m):    # we will do a dfs from starting from every single node of the grid
                for j_start in range(0,n):
                    
                    # do the dfs, comparing the letters on the grid with the letters of the word

                    stack = []
                    
                    seen = set()

                    stack.append( (i_start, j_start, 0, seen) ) # k is the word index

                    while len(stack) > 0:
        
                        i, j, k, seen = stack.pop() # k is the word index

                        if not (i, j) in seen:

                            # seen.add((i,j))
                            
                            if board[i][j] == word[k]: # compare the letter in the grid with the lettern in the kth position of the word. If they are the same, we can continue exploring in out dfs
                                
                                seen.add((i,j))

                                if k == p - 1: # we have reach the end of the word, so we have found it and must return true
                                    return True

                                # explore the adjacent cells. With k+1 we are pointing to the next letter of the word
                                if i + 1 < m:
                                    stack.append( (i+1, j, k+1, seen.copy()) ) # my solution for backtracking the seen set here was tracking it by creating a copy of it, and work on the top of it. If we were implementing dfs recursivelly, we could just do see.remove((i,j)) after the recursive call. Thal would be faster and save tons of memory. How to do it efficiently here in the iterative implementation?
                                if i - 1 >= 0:
                                    stack.append( (i-1, j, k+1, seen.copy()) )
                                if j + 1 < n:
                                    stack.append( (i, j+1, k+1, seen.copy()) )
                                if j - 1 >= 0:
                                    stack.append( (i, j-1, k+1, seen.copy()) )
                                

            return False
        

        def Solution2(board, word):
            # lets do it recursively. It might be faster because o the backtracking, without the need of copyng the seen array.

            # OPTIMIZATIONS
            # R = len(board)
            # C = len(board[0])
            
            # if len(word) > R*C:
            #     return False
            
            # count = Counter(sum(board, []))
            
            # for c, countWord in Counter(word).items():
            #     if count[c] < countWord:
            #         return False
            # if count[word[0]] > count[word[-1]]:
            #     word = word[::-1]



            m = len(board)
            n = len(board[0])
            p = len(word)

            if p > m*n:
                return False
            
            def dfs(i,j,k):

                if k >= p: # we have reach the end of the word, so we have found it and must return true
                    return True

                if (i, j) in seen :
                    return False
                
                if i >= m or i < 0 or j >= n or j < 0: 
                    return False
                
                if board[i][j] == word[k]:

                    seen.add((i,j))

                    a, b, c, d = False, False, False, False

                   
                    a = dfs(i+1, j, k+1) 
                   
                    b = dfs(i-1, j, k+1) 
                   
                    c = dfs(i, j+1, k+1) 
                   
                    d = dfs(i, j-1, k+1)

                    seen.remove((i,j)) # backtracking

                    if a == True or b == True or c == True or d == True:
                        return True

                return False



            for i_start in range(0,m):    # we will do a dfs from starting from every single node of the grid
                for j_start in range(0,n):
                    # do the dfs, comparing the letters on the grid with the letters of the word
                    seen = set()

                    flag = dfs(i_start,j_start,0)

                    if flag == True:
                        return True

            return False


        return Solution2(board, word)