# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/odd-even-linked-list/submissions/1361652722/?envType=study-plan-v2&envId=leetcode-75
        # keep a pointer to the last even. As we find a new eve, we place that even in front ot the last even.
        dummy = ListNode(0, head)
        node = dummy
        lastOdd = dummy
        i = 0
        while node:
            if i % 2 == 1:
                nextNode = node.next 
                prev.next = node.next 
                node.next = lastOdd.next
                lastOdd.next = node
                lastOdd = node
                node = nextNode
            else:
                prev = node 
                node = node.next
            i += 1

        return dummy.next
