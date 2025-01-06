# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # https://leetcode.com/problems/unique-binary-search-trees-ii/?envType=problem-list-v2&envId=tree
        # 
        # bottom up apporach with dp. We will build the smalest subtrees, of window size of 0, 1, 2, 3 .... till we reach a  souluiton of n - 1
        # this works because the solutions of size 3 for xemple, uses the solutions of sizes 2,1 and 0. Ans so on. 
        
        dp = {}
        # base case
        for num in range(1,n+1):
            dp[(num,num-1)] = [None] # solutions with size -1, that is only None
            dp[(num+1,num)] = [None] # solutions with size -1, that is only None
            dp[(num,num)] = [TreeNode(num)] # slutions with size 0, that is only one node

        for size in range(1,n):
            for l in range(1, n+1 - size):
                r = l + size
                dp[(l,r)] = []
                for nodeVal in range(l, r+1): # select a node within the interval ans split the tree into subtrees of size < current size. All of these solutions will be already in the dp
                    leftSolutions = dp[(l, nodeVal-1)] # all the solutions of size < current size will be already in the dp, so we can get from it directly
                    rightSolutions = dp[(nodeVal+1, r)]
                    # combine both sides
                    for leftSolution in leftSolutions:
                        for rightSolution in rightSolutions:
                            node = TreeNode(nodeVal, leftSolution, rightSolution)
                            dp[(l,r)].append(node)

        return dp[(1,n)]



        # def backtrack(l, r):
        #     # return number of combinations of the sub branch
        #     if l == r: # base case
        #         return 1
        #     combTotal = 0
        #     for cur in range(l, r+1):
        #         # chose a current node with the interval, and split the tree into the left and right branches
        #         combLeft = backtrack(l, cur-1) # left branch
        #         combRight = backtrack(cur+1, r) # right branch
        #         combCur = combLeft * combRight
        #         combTotal += combCur
        #     return combTotal
        
        # combinations = backtrack(1, n)

        # return combinations