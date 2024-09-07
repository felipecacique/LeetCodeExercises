# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/?envType=daily-question&envId=2024-09-06
        
        nums = set(nums)
        dummy = ListNode(0, head)
        node = dummy.next
        prev = dummy
        while node:
            if node.val in nums:
                prev.next = node.next
                node = prev.next
            else:
                prev = node
                node = node.next

        return dummy.next