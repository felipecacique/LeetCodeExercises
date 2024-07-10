# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/minimum-absolute-difference-in-bst/?envType=study-plan-v2&envId=top-interview-150

        # minimum = [int("inf")]

        # def getMaxMin(node):

        #     if not node:
        #         return None, None, None

        #     if node.left == None and node.right == None:
        #         return node.val, node.val, node.val

        #     min_left_from_left, left, max_right_from_left = getMaxMin(node.left)
        #     min_left_from_right, right, max_right_from_right = getMaxMin(node.right)

        #     minimum[0] = min(minimum[0], node.val - left)
        #     if max_right_from_left: minimum[0] = min(minimum[0], node.val - max_right_from_left)
        #     minimum[0] = min(minimum[0], right - node.val )
        #     if max_right_from_left: minimum[0] = min(minimum[0], max_right_from_right - node.val)

        #     return min_left_from_left, node.val, max_right_from_right


        minimum = [float("inf")]

        def dfs(node, val_min, val_max, val_parent):

            if not node:
                return

            if val_min != node.val:
                minimum[0] = min(minimum[0], abs(val_min-node.val))
                minimum[0] = min(minimum[0], abs(val_max-node.val))
                minimum[0] = min(minimum[0], abs(val_parent-node.val))

            dfs(node.left, min(node.val, val_min), node.val, node.val)
            dfs(node.right, node.val, max(node.val, val_max), node.val)
        
        dfs(root, root.val, root.val, root.val)

        return minimum[0] 
