# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #https://leetcode.com/problems/palindrome-linked-list/?envType=study-plan-v2&envId=top-100-liked
        # time O(n) space o(1)
        # find the middle of the list, reverse the second half, compare

        # find the middle
        fast, slow = head, head
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        middle = slow
        
        # reverse the second half
        while slow:
            nex = slow.next
            slow.next = prev
            prev = slow
            slow = nex
        
        # compare the nodes of the first half with the second half
        node = head
        while middle:
            if node.val != middle.val: 
                return False
            node = node.next
            middle = middle.next

        return True
