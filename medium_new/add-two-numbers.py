
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/add-two-numbers/?envType=study-plan-v2&envId=top-interview-150
        def Solution1(l1,l2):
            # get number 1
            nums1 = []
            while l1:
                nums1.append(l1.val)
                l1 = l1.next
            
            # get number 2
            nums2 = []
            while l2:
                nums2.append(l2.val)
                l2 = l2.next
            
            # number 1 list to float
            num1 = 0
            for i in range(len(nums1)):
                num1 += nums1[i] * 10**i

            # number 2 list to float
            num2 = 0
            for i in range(len(nums2)):
                num2 += nums2[i] * 10**i
        
            # lets sum the numbers
            num_sum = num1 + num2

            # num to arr
            sum_list = list(str(num_sum))
            sum_list = reversed(sum_list)

            # arr to a linked list
            head = ListNode()
            node = head
            for num in sum_list:
                node.next = ListNode(int(num))
                node = node.next 
            head = head.next

            return head
        
        def Solution2(l1,l2):
            # great solution! doing the sum as we traverse the lists. Inpired in a solution from submissions

            dummy = ListNode()
            node = dummy
            carry = 0

            while l1 or l2 or carry:

                val1 = l1.val if l1 else 0
                val2 = l2.val if l2 else 0

                sum_ = val1 + val2 + carry
                carry = sum_//10
                val = sum_%10

                node.next = ListNode(val)

                node = node.next 
                if l1: l1 = l1.next
                if l2: l2 = l2.next

            return dummy.next

        return Solution2(l1,l2)