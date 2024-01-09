# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # lets do a dfs in order transversal. Lets count the nodes from the top to the bottom
        max_count = [0]

        def dfs(node, count):
            if not node:
                if count > max_count[0]:
                    max_count[0] = count
                return

            dfs(node.left, count + 1)
            dfs(node.right, count + 1)

            return

        dfs(root, 0)

        return max_count[0]
