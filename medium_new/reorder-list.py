# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # https://leetcode.com/problems/reorder-list/?envType=problem-list-v2&envId=linked-list
        # time O(n) space(1)
        # Find the middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nex = second.next
            second.next = prev
            prev = second
            second = nex
    
        # Merge the two halves
        first = head
        second = prev
        while second:
            firstNext, secondNext = first.next, second.next
            first.next = second
            second.next = firstNext
            first, second = firstNext, secondNext
        