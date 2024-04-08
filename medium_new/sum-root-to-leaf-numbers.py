# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
        sum_ = [0]
        def sumNumbersHelper(root, number):
            if not root:
                return 
            number = number + str(root.val)
            if not root.left and not root.right: # is leaf node
                sum_[0] += int(number) 
            sumNumbersHelper(root.left, number)
            sumNumbersHelper(root.right, number)
            return

        sumNumbersHelper(root, '')

        return sum_[0]
        
