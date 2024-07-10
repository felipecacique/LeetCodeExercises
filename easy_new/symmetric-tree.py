# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150
        # similar to the problem same-tree
        
        def isSymmetricTree(p, q):
            if p is None and q is None: return True
            if p is None and q is not None: return False
            if p is not None and q is None: return False

            if p.val != q.val: return False

            return isSymmetricTree(p.left, q.right) and isSymmetricTree(q.left, p.right)
        
        return isSymmetricTree(root.left, root.right)