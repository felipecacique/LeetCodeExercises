# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Lets travel both lists simulteneously. We start by comparing the first element of each list. If list1[i] <= list2[j] then add list1[i] to mergedList and compare the next element list1[i+1] to list2[j]. We stop when we get in the end of both lists.

        def Solution1(list1, list2):
            # time O(m+n) space O(m+n)

            # Handling base cases
            mergedList = ListNode()  # create first node
            mergedListRoot = mergedList  # create our pointer to the root

            while 1:
                if list1 == None and list2 == None:  # we got to the end of both lists
                    break

                if list2 == None or (list1 != None and list1.val <= list2.val):
                    newNode = ListNode(list1.val)  # create a new node
                    mergedList.next = newNode  # add node to the mergedLinked list
                    mergedList = mergedList.next  # point to the last list node
                    list1 = list1.next  # point to the next node of list1

                elif list1 == None or (list2 != None and list2.val <= list1.val):
                    newNode = ListNode(list2.val)  # create a new node
                    mergedList.next = newNode  # add node to the mergedLinked list
                    mergedList = mergedList.next  # point to the last list node
                    list2 = list2.next  # point to the next node of list2

            return mergedListRoot.next

        return Solution1(list1, list2)


# if we remove de Solution1 the code runs quickly
