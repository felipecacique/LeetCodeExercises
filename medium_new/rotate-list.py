# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # https://leetcode.com/problems/rotate-list/submissions/1316980173/?envType=study-plan-v2&envId=top-interview-150
        # time complexity O(n)
        
        if k == 0 or not head:
            return head 

        n = 0
        node = head
        while node: # get the list size
            node = node.next
            n += 1
        
        k = n - k % n # get the idx that has to be the new head

        if k == 0 or k == n:
            return head

        i = 0
        node = head
        first_node = node
        while node:
            if i == k:
                # found the new head
                head = node
                prev_node.next = None
            
            if node.next is None: # last node
                node.next = first_node # last node points to the first node
                break

            i += 1
            prev_node = node
            node = node.next

        return head