# https://leetcode.com/problems/binary-tree-level-order-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Solution1: do dfs, calculate the height, and append its nodes based on the height like that: res[height].append(node.value). Time O(n)

        def Solution1(root):
            res = []

            def dfs(node, height):
                if node:
                    if len(res) <= height:
                        res.append([])
                    res[height].append(node.val)

                if not node:
                    return

                dfs(node.left, height + 1)
                dfs(node.right, height + 1)

                return

            dfs(root, 0)

            return res

        return Solution1(root)
