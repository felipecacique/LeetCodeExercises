# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do a dfs untill we reach the first leaf, that is the smallest element. We start counting by there, and we continue doing our dfs. Note if we do a inorder traversal, we we reach the nodes in a sorted way. 

        index = [0]
        val = [None]
        
        def dfs(node):

            if not node:
                return None
            
            if dfs(node.left): 
                return True
                    
            # process current node
            index[0] += 1
            val[0] = node.val
            if index[0] == k:
                    return True

            if dfs(node.right):
                return True

            return False
        
        dfs(root)

        return val[0]