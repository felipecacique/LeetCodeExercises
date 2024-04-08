# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150

        max_path = [float('-inf')]
        def maxPathSumHelper(root):

            if not root:
                return 0

            max_left = maxPathSumHelper(root.left)
            max_right = maxPathSumHelper(root.right)
            
            max_path_node = max(root.val, max_left + root.val, max_right + root.val) # max path from its children with with this node as a head
            max_path[0] = max(max_path[0], max_path_node, max_left + root.val + max_right)

            return max_path_node

        maxPathSumHelper(root)

        return max_path[0]
