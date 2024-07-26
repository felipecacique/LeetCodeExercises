# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # shift all nodes to the left and delete the tail
        
        curr = node
        while curr:
            # Shift the next node values to the prev node 
            if curr.next:  
                curr.val = curr.next.val
            # Remove the tail
            if not curr.next.next:
                 curr.next = None
            curr = curr.next