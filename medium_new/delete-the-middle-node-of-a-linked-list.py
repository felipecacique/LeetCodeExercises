# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/?envType=study-plan-v2&envId=leetcode-75
        # get the linked list size n
        
        def Solution1(): # traversing the list twice, fisrt to calculate the middle, secondly to fing the middle and remove it
            n = 0
            node = head
            while node:
                n += 1
                node = node.next

            # find the linked list smiddle
            import math
            id_middle = math.floor(n/2)
            n = 0
            node = head
            node_prev = None
            while node:
                if n == id_middle: # remove middle from list
                    if not node_prev:
                        return None
                    node_prev.next = node.next
                    break
                n += 1
                node_prev = node
                node = node.next

            return head
        

        def Solution2(): # using 2 pointers to traverse the list, a fast and a slow. When the fast reaches the end, the slow will b in the middle

            if not head or not head.next: return 
            fast = head.next.next # if we do fast = head, the algorithm does to jump the middle, but might be one node after or before 
            slow = head

            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            if slow.next:
                slow.next = slow.next.next # if fast reached the end, slow will be one nove before the meddle, and we jump the middle 

            return head


        return Solution2()