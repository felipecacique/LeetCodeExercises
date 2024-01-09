# https://leetcode.com/problems/balanced-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Solution 1 - travel the tree twice. First for calculating the branches height for every node, storing its value within the node. Sencondly we travel it again comparing for value of height for every left and right nodes. If we find a difference in hight greatter than 1, then the tree is not height-balanced.

        # Solution 2 - one travel. lets count the tree height from the root to bottom. The distance of the node from the root. The we compare the leaves height only. If we find a difference in hight greatter than 1, then the tree is not height-balanced. We can get the max and min height of the leaves, and compare these 2 values. time O(n) since we have to reach every leaf. This solution will only work for a tree with 2 or more leaves. I will need to handle this last situation. A tree with a single node with height greatter than 2, is not balanced. It did not worked ... many failing cases

        # Solution 3 - travel the tree once. We star calculating the height from the leaves to the top. For a given node, we hget the left and right heights, and compare them. After we calculate ne node's height (its height from the its deepest branch) given by height = max(left_height, right_height) + 1.  In other owers, every node will store the distance between them and the deepest leaf. That is the height. time O(n) space O(n)

        def Solution3(root):
            mark = [True]

            def dfs(node):
                if not node:
                    return 0

                l_height = dfs(node.left)
                r_height = dfs(node.right)

                if abs(l_height - r_height) > 1:
                    mark[0] = False

                height = max(l_height, r_height) + 1

                return height

            dfs(root)

            return mark[0]

        return Solution3(root)
