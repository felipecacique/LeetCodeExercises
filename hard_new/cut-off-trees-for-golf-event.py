class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # https://leetcode.com/problems/cut-off-trees-for-golf-event/
        # time O(m*n*m*n)
        
        m = len(forest)
        n = len(forest[0])

        # Cheq if we could possibly visit all tree cells
        # get the set with the trees we can visit
        from collections import deque
        queue = deque([(0,0)])
        seen = set()
        while queue:
            j, i = queue.pop()
            if i + 1 < n and forest[j][i+1] != 0 and (j,i+1) not in seen:
                seen.add((j,i+1))
                queue.append((j,i+1))
            if i - 1 >= 0 and forest[j][i-1] != 0 and (j,i-1) not in seen:
                seen.add((j,i-1))
                queue.append((j,i-1))
            if j + 1 < m and forest[j+1][i] != 0 and (j+1,i) not in seen:
                seen.add((j+1,i))
                queue.append((j+1,i))
            if j - 1 >= 0 and forest[j-1][i] != 0 and (j-1,i) not in seen:
                seen.add((j-1,i))
                queue.append((j-1,i))

        trees = []
        empty = []
        # Get all the trees and its coordinates, and the empty cells
        for j in range(m):
            for i in range(n):
                if forest[j][i] > 1: trees.append((forest[j][i],j,i)) 
                elif forest[j][i] == 1: empty.append((j,i)) 

        zeroes = m*n - (len(trees) + len(empty))
        # Check if we could possibly visit all trees
        if len(seen) < (len(trees) + len(empty)): 
            # we cannot visit all trees
            return -1

        # We will sort the trees in order they must be cut
        trees = sorted(trees)
        trees = deque(trees)
        minStepsTotal = 0
        myposition = (0,0)
        while trees:
            size, jGoal, iGoal = trees.popleft()
            # We could cut the i,j tree, and moved from myposition to the tree position (j,i)
            if zeroes == 0: # there is no zeroes, so w can just do as direct calculation (it is not necessary, but makes the code faster for the cases in which there is not zeroes)
                minStepsTotal += abs(myposition[0] - jGoal) + abs(myposition[1] - iGoal)
                myposition = jGoal, iGoal
                continue
            
            # Get the number of steps between 2 points using BFS
            queue = deque([(0, myposition[0], myposition[1])])
            seen = set()
            minSteps = 0
            while queue:
                steps, j, i = queue.popleft()

                if (j, i) == (jGoal, iGoal):
                    minSteps = steps
                    break
                
                if i + 1 < n and forest[j][i+1] != 0 and (j,i+1) not in seen:
                    seen.add((j,i+1))
                    queue.append((steps+1,j,i+1))
                if i - 1 >= 0 and forest[j][i-1] != 0 and (j,i-1) not in seen:
                    seen.add((j,i-1))
                    queue.append((steps+1,j,i-1))
                if j + 1 < m and forest[j+1][i] != 0 and (j+1,i) not in seen:
                    seen.add((j+1,i))
                    queue.append((steps+1,j+1,i))
                if j - 1 >= 0 and forest[j-1][i] != 0 and (j-1,i) not in seen:
                    seen.add((j-1,i))
                    queue.append((steps+1,j-1,i))

            minStepsTotal += minSteps
            myposition = jGoal, iGoal

        return minStepsTotal


        # trees = []
        # empty = set([(0,0)])

        # # Get all the trees in ist coordinates, and the empty cells
        # m = len(forest)
        # n = len(forest[0])
        # for j in range(m):
        #     for i in range(n):
        #         if forest[j][i] > 1: 
        #             trees.append((forest[j][i],j,i)) 
        #             empty.add((j,i)) 
        #         elif forest[j][i] == 1: empty.add((j,i)) 

        # # We will sort the trees in order they must be cut
        # trees = sorted(trees)
        # from collections import deque
        # trees = deque(trees)
        # print(trees, empty)
        # minSteps = 0
        # myposition = (0,0)
        # while trees:
        #     size, j, i = trees.popleft()
        #     print(size, j, trees, empty)

        #     # Is there an empty space around the tree? i other words, can we reach it? if so, we cut it and add it to empty set
        #     if (j,i+1) in empty: empty.add((j,i)) # we can cut the tree (j,i) because there is at least one empty cell surround it
        #     elif (j,i-1) in empty: empty.add((j,i))
        #     elif (j+1,i) in empty: empty.add((j,i))
        #     elif (j-1,i) in empty: empty.add((j,i))
        #     elif (j,i) in empty: empty.add((j,i)) # condition importatn for the first cell only
        #     else: return -1 # the tree is unreachable

        #     # We could cut the i,j tree, and moved from myposition to the tree position (j,i)
        #     minSteps += abs(myposition[0] - j) + abs(myposition[1] - i)
        #     myposition = j, i


        # return minSteps










        # queue.append((0,0, 0))
        # while queue:
        #     j, i, lastCutSize = queue.popleft()


        # m = len(forest)
        # n = len(forest[0])
        
        # lastCutSize = 0
        # from collections import deque
        # queue = deque([])
        # queue.append((0,0, 0))
        # while queue:
        #     j, i, lastCutSize = queue.popleft()
            
        #     if forest[j][i] == 0:
        #         continue
            
        #     if forest[j][i] > 1:
        #         # Check if we can cut the tree
        #         if forest[j][i] > = lastCutSize:
        #             lastCutSize = forest[j][i]
        #             forest[j][i] = 1
                
        #             # We cut the tree and add its adjascent cells to the queue 
        #             if i-1 >= 0 and forest[j][i-1] != 0 and forest[j][i-1] >= lastCutSize:
        #                 queue.append((j,i-1))
        #             if i+1 < n and forest[j][i+1] != 0 and forest[j][i+1] >= lastCutSize:
        #                 queue.append((j,i+1))
        #             if j-1 >= 0 and forest[j-1][i] != 0 and forest[j-1][i] >= lastCutSize:
        #                 queue.append((j-1,i))
        #             if j+1 < m and forest[j][i+1] != 0 and forest[j+1][i] >= lastCutSize:
        #                 queue.append((j+1,i))
                        
        # # Check if we have cut all trees                
        # for j in range(m):
        #     for i in range(n):
        #         if forest[j][i] > 1:
        #             return -1
        

        # return minSteps 