# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

        def dfs(left, right):
            if left > right:
                return None

            middle = int((left+right)/2)

            node = TreeNode(nums[middle])
            node.left  = dfs(left, middle-1)
            node.right = dfs(middle+1, right)

            return node

        head = dfs(0, len(nums)-1)

        return head
        