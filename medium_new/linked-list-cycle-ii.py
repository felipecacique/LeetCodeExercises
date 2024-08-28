# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/linked-list-cycle-ii/?envType=study-plan-v2&envId=top-100-liked
        # time O(N) space O(1)
        # got the inspiration for the soluion from Solutions and a previous neetcode problem, but i have deduced the equation bu myself. 
        
        # find the first meeting point
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: break
        if not fast or not fast.next: return None

        # walk from the beggining and from the meeting point. They will meet again in the beggining of the loop
        while head != fast:
            head = head.next
            fast = fast.next

        return head