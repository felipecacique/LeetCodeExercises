# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/add-two-numbers-ii/

        # Get first number
        num1 = 0
        cur1 = l1
        while cur1:
            num1 = num1 * 10 + cur1.val
            cur1 = cur1.next

        # Get second number
        num2 = 0
        cur2 = l2
        while cur2:
            num2 = num2 * 10 + cur2.val
            cur2 = cur2.next
        
        # Sum them and convert to string
        num3 = num1 + num2
        num3Str = str(num3)
        
        # Convert the string sum into a linked list
        l3 = ListNode()
        cur3 = l3
        for i, num in enumerate(num3Str):
            cur3.val = int(num)
            if i< len(num3Str) - 1: 
                cur3.next = ListNode()
                cur3 = cur3.next
            
        return l3