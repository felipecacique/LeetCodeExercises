class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # https://leetcode.com/problems/count-submatrices-with-all-ones/
        # traverse the matrix backwards and from each cell stores the (sum_ones_below, sum_ones_right).
        # do this using memoization
        # traverse the matrix again, and through the sums, we can infere the number of retangles
        # O(mxn)
        #   (3,1)(0,0)(1,1)
        #   (2,2)(2,1)(0,0)^
        #   (1,2)(1,1)(0,0)|
        #                <-START
        #
        # combinations
        # this cell (3,1) tells me that staring from it, we have a submatrix 3x1 with all zeroes. Combination is equal to 3.
        # (2,2) ->  4 combinations
        # (1,2) -> 2 combinations
        # what is the formula here??
        # (3,3) -> 6   (1,1)(1,2)(1,3)(2,1)(2,2)(2,3)(3,1)(3,2)(3,3)
        # (4,4) -> 8
        # (x,y) -> x*y
        # (3,2) -> 2*3 - min(3,2)  -- (1,1)(1,2)(2,1)(2,2)(3,1)(3,2)
        # to calculane the number of subs matrices in (x,y) we just do x*y
        # THE EXPLANATION ABOVE WILL NOT WORK, BECAUSE IT DOES NOT HANDLE THE DIAGONAL ZEROES!! A NEW SOLUTION BELLOW!!
        
        # TIME COMPLEXITY: O(m*n*n)
        h = {}
        m = len(mat)
        n = len(mat[0])
        
        zeroes = {}
        for j in range(0,m): # iterate
            for i in range(0,n):

                if mat[j][i] == 1:
                    vertical = h.get((j-1,i), [0])[0] + 1
                    # getting the combinations
                    combinations = vertical
                    if (j,i-1) in h:
                        if vertical >= h[(j,i-1)][0]: 
                            # if vertical >> vertical_left then the combination is the vertical + the combination of the cell on the left
                            combinations += h[(j,i-1)][1]
                        else:
                            # if vertical < vertical_left then we need to backtracts, calculating the combination, which is given by the sum of all left veticals. But we have to keep track of the min vertical (min_vertical) as we move left, and instead of adding the left_vertical to our combinations, we add the min_vertical
                            k = 1
                            min_vertical = vertical
                            while (j,i-k) in h and h[(j,i-k)][0]!=0:
                                min_vertical = min(h[(j,i-k)][0], min_vertical)
                                combinations += min_vertical
                                k += 1
                    h[(j,i)] = (vertical, combinations)
                else:
                     h[(j,i)] = (0,0)

        count = 0
        for key, (vertical, combinations) in h.items():
            count += combinations
        
        return count
            