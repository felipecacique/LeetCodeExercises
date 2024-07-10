# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # https://leetcode.com/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150
        
        if root is None: return False

        if root.left is None and root.right is None: # it is a root
            if targetSum - root.val == 0: 
                return True
    
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)