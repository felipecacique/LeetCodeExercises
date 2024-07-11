# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/?envType=study-plan-v2&envId=top-interview-150

        level_nodes = {}
        def zigzagLevelOrder(root, h):
            if not root:
                return None
            
            level_nodes[h] = level_nodes.get(h, []) + [root.val]
    
            zigzagLevelOrder(root.left, h+1)
            zigzagLevelOrder(root.right, h+1)

        # Get the nodes of each level
        zigzagLevelOrder(root, 0)

        # return a zigzag list of the nodes
        return [ (nodes if level%2==0 else reversed(nodes) ) for level, nodes in level_nodes.items()]