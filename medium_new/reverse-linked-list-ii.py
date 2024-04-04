# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
        # based on the solution of 25. Reverse Nodes in k-Group

        headStart = head
        headStartPre = None
        for _ in range(left-1):
            headStartPre = headStart
            headStart = headStart.next
            
        curr = headStart
        pre = None
        nex = None
        for _ in range(right-left+1):
            nex = curr.next
            curr.next = pre
            pre = curr
            curr = nex
        
        headStart.next = nex
        if headStartPre: headStartPre.next = pre
        else: head = pre

        return head

        