# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we will create and array with the most right side nodes, and each position i in this array corresponde to the height of the three. So there must be the most right node in that height. We can do a normal dfs, and add the values to this array in the position i=height. If there is alredy a value in the i = height, we replace it with new one, which is the most right side node for that height, since the right nodes are visited last. Time O(n)
        
        rightSideVal = []
        def rightSide(node, height):

            if not node:
                return None
           
            if  height < len(rightSideVal):
                rightSideVal[height] = node.val # there is alredy a value in the i = height, so we replace it with new one, which is the most right side node for that height, since the right nodes are visited last
            else:
                rightSideVal.append(node.val)

            rightSide(node.left, height+1)
            rightSide(node.right, height+1)

            return
        
        rightSide(root, 0)


        return rightSideVal