# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/remove-nodes-from-linked-list/?envType=daily-question&envId=2024-05-06
        # itereate backwards. Go to the end of the list by a dfs, post orderr, and return the node (backwards). In post order we append the next_node to the current node(head) by head.next = node only if the head.val > next_node.val. Otherswise we must remove the current node from the list, and just return the next_node. It satisfies the rule and at the nd we will have he function returning the linked list answer.
        
        if not head.next:
            return head
        
        next_node = self.removeNodes(head.next)
        
        if next_node.val > head.val: # then remove head
            return next_node
        
        head.next = next_node
        return head
