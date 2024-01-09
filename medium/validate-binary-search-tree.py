# https://leetcode.com/problems/validate-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # solution1: do a bfs, post order traversal, buttom up, the left and right children of a node will the max and min values respectively.
        # If node.val > left.max and node.val < right.min, then the node's branch is a BST. Update the max and min, and repeat the process. If all branches are BST, then we return True.

        def Solution1(root):

            def dfs(node):

                if not node:
                    return None, None, True
                
                left_max, left_min, left_flag = dfs(node.left)
                if left_flag == False: # it's branch children is not a valid BST branch
                    return False, False, False

                right_max, right_min, right_flag = dfs(node.right)
                if right_flag == False: # it's branch children is not a valid BST branch
                    return False, False, False

                if left_max == None:
                    left_max = -float('inf')
                    left_min = float('inf')

                if right_max == None:
                    right_max = -float('inf')
                    right_min = float('inf')     
            
                if node.val > left_max and node.val < right_min: # it is a valid BST branch
                    return max(node.val, right_max), min(node.val, left_min), True

                else: # it is not a valid BST branch
                    return False, False, False


            mark1, mark2, flag = dfs(root)
            
            if flag == False:
                return False
            else:
                return True    


        def Solution2(root):
            # Solution from https://www.youtube.com/watch?v=s6ATEkipzow&ab_channel=NeetCode
            # the node in the righ must be gratter than all its parents. As we go down in the bsf to the right, we pass the min of its parents, and to the left we pass the max od its parents. In the node we compare the node's value with the max and min of its parents. If right_node.val > min(parents) then not a BST
            # Solution1 is as fast as this one

            def valid(node, left, right):
                if not node:
                    return True # an empty node is a BST
                if not(node.val < right and node.val > left):
                    return False
                return(valid(node.left, left, node.val) and valid(node.right, node.val, right)) 

            return valid(root, float('-inf'), float('inf'))


        return Solution2(root)  