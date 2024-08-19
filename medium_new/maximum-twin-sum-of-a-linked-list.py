# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75
        # time O(n) space O(1)
        
       # find the middle node using slot fast pointers
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow # middle

        # reverse the second half
        prev = None
        while curr:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        curr = prev
        
        # traverse the both linked list simultaneaosly
        sol = 0
        while curr:
            sol = max( sol, curr.val + head.val )
            curr = curr.next
            head = head.next
        
        return sol

