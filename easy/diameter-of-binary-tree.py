# https://leetcode.com/problems/diameter-of-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Solution1: For a given node, the longest distance that pass in this node is given by the longest distance from the left side + the longest distance of th right side. We can do a DFS, post order traversal, going starting cumputing the sistance from the leaf nodes. Its is kind a divide and conquer problem, where we will solve the subproblems nodes(h) from it we calculate the nodes(h-1) and so on through the DFS. Always storing the highest value. Lest say we are in the node k. The biggeste path in the left is given by k.left longest path + k.right longest path. But for k.left the longest path the max(k.left.left, k.left.right), beceuse we can only have one path coming from the node k.left since the path has to go through node k. If the path goes through k, then it would not be possible that this path would go through the k.left.left and k.lef.right. It can only be one of both.

        # Better explanation: The longest distance must have some node as its root (lets call it root_d). If a root_d is the root, then no other nodes from its branch would be a root, and the path would either go through the left or through the right un the subsequent childs. We will do a DFS, post order transversal, and every node will return the longest path from it, suposing it was not the root_d, given by max(k.left.left, k.left.right) + 1. The longest path in which this note is not a root is either a path coming from the left or from the right, plus the node itself. Then we process the node, suposing the the node is the root_d, we calculate the node longest path given by node_longest_path = left_longest_path + right_longest_path. As we go the BFS, we store the largest node_longest_path. This is our diameter.

        def Solution1(root):
            diameter = [-1]

            def dfs(node):
                if not node:
                    return 0

                left_longest_path = dfs(node.left)
                right_longest_path = dfs(node.right)

                # a path in which this node is a root is
                node_longest_path = left_longest_path + right_longest_path
                if node_longest_path > diameter[0]:
                    diameter[0] = node_longest_path

                return (
                    max(left_longest_path, right_longest_path) + 1
                )  # the longest path in which this note is not a root is either a path coming from the left or from the right , plus the node itself

            dfs(root)

            return diameter[0]

        return Solution1(root)
