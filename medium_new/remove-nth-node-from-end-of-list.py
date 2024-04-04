# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1222477360/?envType=study-plan-v2&envId=top-interview-150
        # finding the list size
        listSize = 1
        node = head
        while node:
            node = node.next
            listSize += 1
        listSize -= 1

        ith = listSize - n + 1

        node = head
        count = 1
        while node:
            if ith > 1 and count == ith-1: 
                # we must remove (jump) the ith node
                node.next = node.next.next
                break
            elif ith == 1: 
                # we must remove the first node
                head = node.next
                break
            node = node.next
            count += 1
        
        return head