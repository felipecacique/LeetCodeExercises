# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/maximum-width-of-binary-tree/
        # O(n)
        # for each level we comput the index of the leftmost element and store it in widths, and comput the rightmost element index. The we substract the indexes + 1 per level to find the distances, and get the maximum of all diferences
        widths = {}
        ans = [1]
        def dfs(node, h, i):
            if not node: return
            if h in widths: ans[0] = max(ans[0], i - widths[h] + 1)
            if not h in widths: widths[h] = i
            dfs(node.left, h+1, i*2-1)
            dfs(node.right, h+1, i*2)
        
        dfs(root, 1, 1)
        return ans[0]