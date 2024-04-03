# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # https://leetcode.com/problems/find-largest-value-in-each-tree-row/
        # traverse the tree, put all nodes in an hashtable organized by its tree height. Then get max for each height
        
        heightValues = []
        
        def dfs(node,height):
            if not node:
                return
            
            if height >= len(heightValues):
                heightValues.append(float('-inf'))
            heightValues[height] = max(heightValues[height], node.val)

            left = dfs(node.left, height+1)
            right = dfs(node.right, height+1)
        
        dfs(root,0)
        
        return heightValues