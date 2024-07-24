# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # https://leetcode.com/problems/delete-nodes-and-return-forest/
        # do a dfs, and delete nodes in a post order traversal

        to_delete = set(to_delete)
        output = []

        def delNotes(node, parentVal):
            if not node:
                return None
            
            if parentVal in to_delete and not node.val in to_delete:
                output.append(node)

            node.left = delNotes(node.left, node.val)
            node.right = delNotes(node.right, node.val)
            if node.val in to_delete:
                return None
            return node

        root = delNotes(root, 0)
        if root: output.append(root)
        
        return output