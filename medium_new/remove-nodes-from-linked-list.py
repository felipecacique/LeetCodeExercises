# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/remove-nodes-from-linked-list/?envType=daily-question&envId=2024-05-06

        if not head.next:
            return head
        
        node = self.removeNodes(head.next)
        
        if node.val > head.val: # then remove head
            return node
        
        head.next = node
        return head
