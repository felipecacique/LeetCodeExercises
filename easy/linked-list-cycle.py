# https://leetcode.com/problems/linked-list-cycle/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # travel the list marking each node already visited as "visited". If we ever fing a node with "visited", then we have a cycle. time O(n) space O(n)

        node = head
        while node:
            if node.val == "visited":
                return True

            node.val = "visited"
            node = node.next

        return False
