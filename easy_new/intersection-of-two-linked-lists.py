# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #https://leetcode.com/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=top-100-liked
        # solution from neetcode
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

# work well but space not o(1)  
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         # https://leetcode.com/problems/intersection-of-two-linked-lists/?envType=study-plan-v2&envId=top-100-liked
#         nodesRef = set()
#         while headA:
#             nodesRef.add(headA)
#             headA = headA.next

#         while headB:
#             if headB in nodesRef:
#                 return headB
#             headB = headB.next
        
#         return None
        

