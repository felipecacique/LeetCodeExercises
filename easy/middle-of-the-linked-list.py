# https://leetcode.com/problems/middle-of-the-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count

        length = getLength(head)

        middle = (length + 1) / 2

        count = 0
        node = head
        while node:
            count += 1
            if count >= middle:
                return node
            node = node.next
        return None
