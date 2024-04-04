# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150

        def Solution1(head,k): # works correctly, but it is too long, complicated and is slow ...
            if k == 1:
                return head

            node1 = ListNode(0, head) # add an extra node on the left
            node2 = node1
            
            def reverseList(node1, node2, head, k): 
                # sort linked list starting from node1.next to node2.next (inclusing) 
                i1 = 0
                ishead = True
                k_ = k
                # i1 pointing to the start-1, and i2 pointing to start+k-1. Now we move i1 to the right and i2 to the left
                while i1 < k//2: # we will exchange with i2+1
                    node1_next_copy = ListNode(node1.next.val)
                    node2_next_copy = ListNode(node2.next.val)
                    
                    node1_next_copy.next = node2.next.next
                    node2.next = node1_next_copy
                    node2_next_copy.next = node1.next.next
                    node1.next = node2_next_copy           
                
                    if ishead:
                        head = node1
                        ishead = False
                    
                    node1 = node1.next
                    node2 = node1
                    i1 += 1
                    i2 = i1
                    k_-=2
                    while i2 < i1+k_-1:
                        node2 = node2.next
                        i2 += 1
                    
                return head
            
            listSize = 1
            node = head
            while node:
                node = node.next
                listSize += 1
            listSize -= 1

            i1 = 0
            i2 = 0
            start = 0
            list_size = listSize
            ishead = True
            head_ = None
            a = 0

            while start + k-1 < list_size:
                i2 = i1
                while i1 < start:
                    node1 = node1.next
                    i1 += 1
                
                while i2 < i1+k-1:
                    node2 = node2.next
                    i2 += 1
                
                m = head_
                while m:
                    m = m.next

                node = reverseList(node1, node2, head, k)
                node1 = node
                node2 = node1
                start += k

                if ishead:
                    head_ = node1
                    ishead = False

            return head_.next
        
        def ReverseKGroup(head,k):
            # from https://www.youtube.com/watch?v=1UOPsfP85V4&ab_channel=NeetCode
            # actually the solution bellow is based on a solution from the submitions. I undertood and rewrited without looking at it. Very intesresting solution
            
            curr = head
            for _ in range(k):
                if not curr:
                    return head
                curr = curr.next
                
            curr = head
            pre = None
            for _ in range(k):
                nex = curr.next
                curr.next = pre
                pre = curr
                curr = nex
            
            head.next = ReverseKGroup(curr,k)
            return pre

        return ReverseKGroup(head,k)
        
