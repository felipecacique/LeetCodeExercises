# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75

        def getSequence(node):
            
            sequence = []

            def dfs(node):

                if not node:
                    return None
                
                valLeft = dfs(node.left)
                valRight = dfs(node.right)

                if valLeft == None and valRight == None:
                    # it is a leaf
                    sequence.append(node.val) 
                
                return node.val
            
            dfs(node)

            return sequence
    
        if getSequence(root1) == getSequence(root2):
            return True
        else:
            return False


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
#         # https://leetcode.com/problems/leaf-similar-trees/?envType=study-plan-v2&envId=leetcode-75

#         def dfs(node, sequence):

#             if not node:
#                 return None, sequence
            
#             valLeft, sequenceLeft = dfs(node.left, sequence)
#             valRight, sequenceRight = dfs(node.right, sequence)
#             sequence = sequenceLeft + sequenceRight

#             if valLeft == None and valRight == None:
#                 # it is a leaf
#                 sequence.append(node.val) 
            
#             return node.val, sequence
        
#         _, sequence1 = dfs(root1,[])
#         _, sequence2 = dfs(root2,[])

#         if sequence1 == sequence2:
#             return True
#         else:
#             return False
        