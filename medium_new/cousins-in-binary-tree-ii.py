# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/cousins-in-binary-tree-ii/?envType=daily-question&envId=2024-11-22
        # O(n)
        def createTable(node, parent, h):
            if not node:
                return
            
            if not h in table: table[h] = {"total":0}
            table[h]["total"] += node.val

            createTable(node.left, node, h+1)
            createTable(node.right, node, h+1)
        
        def changeTree(node, valBrother, parent, h):
            if not node:
                return
            
            sum_cousin = table[h]["total"] - node.val
            if valBrother: sum_cousin -= valBrother
            node.val = sum_cousin

            node_right_val = node.right.val if node.right else 0
            node_left_val = node.left.val if node.left else 0

            changeTree(node.left, node_right_val, node, h+1)
            changeTree(node.right, node_left_val,  node, h+1)
        
        table = {}
        createTable(root, 0, 0)
        changeTree(root, 0, 0, 0)

        return root




        # def createTable(node, parent, h):
        #     if not node:
        #         return
            
        #     if not h in table: table[h] = {"total":0}
        #     if not parent in table[h]: table[h][parent] = []
        #     table[h][parent].append(node.val)
        #     table[h]["total"] += node.val

        #     createTable(node.left, node, h+1)
        #     createTable(node.right, node, h+1)
        
        # def changeTree(node, parent, h):
        #     if not node:
        #         return
            
        #     sum_cousin = table[h]["total"] 
        #     if h in table and parent in table[h]:
        #         sum_cousin -= sum(table[h][parent])

        #     node.val = sum_cousin

        #     changeTree(node.left, node, h+1)
        #     changeTree(node.right, node, h+1)
        
        # table = {}
        # createTable(root, 0, 0)
        # changeTree(root, 0, 0)

        # return root



