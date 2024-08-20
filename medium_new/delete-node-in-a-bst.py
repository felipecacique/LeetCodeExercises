# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # https://leetcode.com/problems/delete-node-in-a-bst/?envType=study-plan-v2&envId=leetcode-75
        # O(height) got solution from https://www.youtube.com/watch?v=LFzAoJJt92M
        # I understood and rewrote by memory
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # search the smallest from the right branch
            curr = root.right
            while curr.left:
                curr = curr.left
            # replace root val
            root.val = curr.val
            # delete node
            root.right = self.deleteNode(root.right, root.val)
        return root

