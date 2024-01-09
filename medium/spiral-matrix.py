# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # start from the first position, and move to the right until it gets to the end or find an already visited cell. Then move down, left, up, right ... and so on. We will use a state machine.

        solution = []

        m = len(matrix)
        n = len(matrix[0]) 

        i, j = 0, 0 # initial point

        state = 'right'

        while len(solution) < m*n:

            # move right
            if state == 'right':
                if j >= n or matrix[i][j] == 'visited':
                    state = 'down'
                    j -= 1
                    i += 1
                else:
                    solution.append(matrix[i][j])
                    matrix[i][j] = 'visited'
                    j += 1

            # move down
            elif state == 'down':
                if i >= m or matrix[i][j] == 'visited':
                    state = 'left'
                    i -= 1
                    j -= 1
                else:
                    solution.append(matrix[i][j])
                    matrix[i][j] = 'visited'
                    i += 1
            
            # move left
            elif state == 'left':
                if j < 0 or matrix[i][j] == 'visited':
                    state = 'up'
                    j += 1
                    i -= 1
                else:
                    solution.append(matrix[i][j])
                    matrix[i][j] = 'visited'
                    j -= 1
            
            # move up
            elif state == 'up':
                if i < 0 or matrix[i][j] == 'visited':
                    state = 'right'
                    i += 1
                    j += 1
                else:
                    solution.append(matrix[i][j])
                    matrix[i][j] = 'visited'
                    i -= 1
                
        return solution

