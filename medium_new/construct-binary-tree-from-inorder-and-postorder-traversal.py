# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/?envType=study-plan-v2&envId=top-interview-150
        # inspired by the solution of 105. Construct Binary Tree from Preorder and Inorder Traversal
        
        if not inorder or not postorder:
            return None

        head = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])

        head.left = self.buildTree(inorder[:index], postorder[:index])
        head.right = self.buildTree(inorder[index+1:], postorder[index:-1])

        return head

