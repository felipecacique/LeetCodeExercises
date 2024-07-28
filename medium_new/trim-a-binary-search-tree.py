# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # https://leetcode.com/problems/trim-a-binary-search-tree/submissions/1336597383/
        
        def dfs(node):
            if not node:
                return None
            if node.val < low: 
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:    
                node.left = dfs(node.left)
                node.right = dfs(node.right)
            return node
        
        return dfs(root)