# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/?envType=study-plan-v2&envId=top-interview-150

        seen = set()
        duplicates = set()

        # get the duplicates
        node = head
        while node:
            if node.val in seen:
                duplicates.add(node.val)
            seen.add(node.val)
            node = node.next

        # remove duplicates
        dummy = ListNode(-1000)
        dummy.next = head
        node = dummy.next
        prev = dummy
        while node:
            if node.val in duplicates:
                prev.next = node.next
                node = node.next
                continue
            prev = node
            node = node.next

        return dummy.next