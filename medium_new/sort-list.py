# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # https://leetcode.com/problems/sort-list/?envType=study-plan-v2&envId=top-interview-150
        # divide and conquer. divide in sub lists, merge together inverting sides
        # O(nlogn)

        if head == None:
            return head

        arr = []
        def dfs(node):
            if not node: return
            arr.append(node.val)
            dfs(node.next)

        dfs(head)
        arr = sorted(arr)

        head = ListNode(arr[0])
        node = head
        for val in arr[1:]:
            node.next = ListNode(val)
            node = node.next

        return head

