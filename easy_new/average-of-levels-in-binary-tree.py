# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # https://leetcode.com/problems/average-of-levels-in-binary-tree/?envType=study-plan-v2&envId=top-interview-150

        val_per_level = {}
        
        def dfs(root, height):

            if root is None: return

            val_per_level[height] = val_per_level.get(height, []) + [root.val]

            dfs(root.left, height+1)
            dfs(root.right, height+1)

        dfs(root, 0)
        
        output = []
        for key, item in val_per_level.items():
            output.append(mean(item))

        return output

            