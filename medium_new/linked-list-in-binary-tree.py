# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        # https://leetcode.com/problems/linked-list-in-binary-tree/?envType=daily-question&envId=2024-09-07
        # o(n*m)

        def dfs(root, nodes):

            # point to the next node for each node in nodes
            newNodes = set()
            for node in nodes:
                node = node.next
                if not node: return True # all the nodes from the list matched with the nodes from tree. That means we found a path
                if root and node.val == root.val: newNodes.add(node)
            nodes = newNodes

            if not root: return False

            # add the root to the set()
            if root.val == head.val: nodes.add(head)

            # if dfs(root.left, nodes.copy()) == True or dfs(root.right, nodes.copy()) == True: 
            if dfs(root.left, nodes) == True or dfs(root.right, nodes) == True: # we dont need to do copy() because as we create a newNodes set, we are already copying the elements, and not modifying the received nodes set
                return True
            
            return False
        
        return dfs(root, set([]))