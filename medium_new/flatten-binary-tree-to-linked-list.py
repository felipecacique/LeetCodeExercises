# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # https://leetcode.com/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150
        # we flatten the left brach, returning a linked list, and traverse this list untill the end, and add to the end the flatten right branch. An in the beggining of the list add the current node
        
        if not root:
            return None

        node = TreeNode(root.val)
        head = node

        node.right = self.flatten(root.left) # get the left linked list
        while node: # go to the end of the linked list
            if node.right == None:
                node.right = self.flatten(root.right) # append the rioght list in the end of the left linked list
                break
            node = node.right
        
        # the answer must be inplace, making the changes in the original root
        root.right = head.right
        root.left = None
    
        return head