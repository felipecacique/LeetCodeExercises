"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # https://leetcode.com/problems/construct-quad-tree/?envType=study-plan-v2&envId=top-interview-150
        # use divide and conquer paradigm

        def construct(jstart, jend, istart, iend):

            # Check if base case
            if jend - jstart == 1:
                node = Node(grid[jstart][istart], True, None, None, None, None)
                return node

            node = Node(0, False, None, None, None, None)
            
            # Divide the grid into 4 quads and call the recursive function
            topLeft = construct(jstart, (jstart+jend)//2, istart, (istart+iend)//2)
            topRight = construct(jstart, (jstart+jend)//2, (istart+iend)//2, iend)
            bottomLeft = construct((jstart+jend)//2, jend, istart, (istart+iend)//2)
            bottomRight = construct((jstart+jend)//2, jend, (istart+iend)//2, iend)

            # Check if they are all leafs and if they are all one's or zeroe's
            if topLeft.val + topRight.val + bottomLeft.val + bottomRight.val in [4, 0] and topLeft.isLeaf + topRight.isLeaf + bottomLeft.isLeaf + bottomRight.isLeaf == 4:
                # The current node can be a leaf of value topLeft.val
                node.val, node.isLeaf, node.topLeft, node.topRight, node.bottomLeft, node.bottomRight = topLeft.val, True, None, None, None, None
            else:
                node.val, node.isLeaf, node.topLeft, node.topRight, node.bottomLeft, node.bottomRight = 1, False, topLeft, topRight, bottomLeft, bottomRight

            return node

        n = len(grid)
        return construct(0, n, 0, n)
