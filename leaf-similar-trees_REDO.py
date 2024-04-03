# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # https://leetcode.com/problems/leaf-similar-trees/
        def dfs(node,leafs,val):
            if not node:
                return None
            
            leafsLeft = dfs(node.left, leafs, node.val)
            leafsRight = dfs(node.right, leafs, node.val)
            
            if not leafsLeft and not leafsRight: 
                leafs.append(node.val)

                
            return leafs
        
        if dfs(root1,[],0) == dfs(root2,[],0):
            return True
        else:
            return False