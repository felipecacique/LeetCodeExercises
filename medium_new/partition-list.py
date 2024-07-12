# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # https://leetcode.com/problems/partition-list/?envType=study-plan-v2&envId=top-interview-150
        # time complexity O(n) space complexity O(n)
        # create 2 copies of the linked list, one with the left nodes, and the other of the right nodes. Then link them together

        dummy_left = ListNode()
        dummy_right = ListNode()

        node_left = dummy_left
        node_right = dummy_right
        node = head
        while node:
            if node.val < x:
                # node_left.next = ListNode(node.val)
                node_left.next = node
                node_left = node_left.next
            else:
                # node_right.next = ListNode(node.val)
                node_right.next = node
                node_right = node_right.next
            node = node.next
        
        node_right.next = None
        node_left.next = dummy_right.next
        return dummy_left.next
        