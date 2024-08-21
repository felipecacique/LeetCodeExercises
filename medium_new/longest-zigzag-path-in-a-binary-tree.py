# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
        def dfs(node, count, lastDir):
            if not node: return count
            l = dfs(node.left, count+1 if lastDir == 'right' else 0, "left")
            r = dfs(node.right, count+1 if lastDir == 'left' else 0, "right")
            return max(l, r)
        return dfs(root, 0, "")

# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         # https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
#         self.sol = 0
#         def dfs(node, count, lastDir):
#             self.sol = max(self.sol, count)
#             if not node: return
#             dfs(node.left, count+1 if lastDir == 'right' else 0, "left")
#             dfs(node.right, count+1 if lastDir == 'left' else 0, "right")
#         dfs(root, 0, "")
#         return self.sol