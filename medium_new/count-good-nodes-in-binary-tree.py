# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, valMax=float('-inf')) -> int:
        # https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75
        
        if not root:
            return 0 
            
        countLeft = self.goodNodes(root.left, max(root.val, valMax))
        countRight = self.goodNodes(root.right, max(root.val, valMax))
        
        count = countLeft + countRight
        if root.val >= valMax:
            count += 1
        
        return count
        