# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # https://leetcode.com/problems/same-tree/?envType=study-plan-v2&envId=top-interview-150

        if p is None and q is None: return True
        if p is None and q is not None: return False
        if p is not None and q is None: return False

        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # if not self.isSameTree(p.left, q.left) or not self.isSameTree(p.right, q.right):
        #     return False
        # return True