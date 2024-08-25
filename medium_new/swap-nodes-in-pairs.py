# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/swap-nodes-in-pairs/?envType=study-plan-v2&envId=top-100-liked
        
        root = head
        dummy = ListNode(0, root)
        head = dummy
        while head and head.next and head.next.next:
            head2 = head.next 
            head3 = head.next.next 
            head4 = head.next.next.next 

            head.next = head3
            head3.next = head2
            head2.next = head4

            head = head.next.next 

        return dummy.next

            
        

        