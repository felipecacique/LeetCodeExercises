# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75
        # simular to a pointer's problem in alist, but with a tree instead
        # is is similar to he commented sol bellow, but with an optimization. I based it in one of the Solutions tutorial
        sol = [0]
        def dfs(node, oldPathSums, currPathSum):
            if not node:
                return False

            currPathSum += node.val
            sol[0] += oldPathSums.get(currPathSum - targetSum, 0)
            oldPathSums[currPathSum] = oldPathSums.get(currPathSum, 0) + 1

            dfs(node.left, oldPathSums, currPathSum)
            dfs(node.right, oldPathSums, currPathSum)

            oldPathSums[currPathSum] -= 1

        dfs(root, {0:1}, 0)

        return sol[0]


# work but a bit slow
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         # https://leetcode.com/problems/path-sum-iii/?envType=study-plan-v2&envId=leetcode-75
#         # simular to a pointer's problem in alist, but with a tree instead
#         sol = [0]
#         def dfs(node, sumPath):
#             if not node:
#                 return False

#             newSumPath = {node.val:1}
#             for path, count in sumPath.items():
#                 newSumPath[path+node.val] = newSumPath.get(path+node.val, 0) + count
#             sumPath = newSumPath

#             if targetSum in sumPath: sol[0] += sumPath[targetSum]

#             dfs(node.left, sumPath.copy())
#             dfs(node.right, sumPath.copy())
            
        
#         dfs(root, {})

#         return sol[0]
