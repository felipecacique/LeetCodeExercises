# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
        # find the middle, divide the list in half. The middle is the parent node, the left part is the left branch, and the right part is the right branch

        if not head:
            return None

        # walk untill through the list untill we reach the end, using fast and slow pointers method
        prev_slow = None
        slow = head
        if head.next:
            fast = head
            while fast and fast.next:
                prev_slow = slow
                slow = slow.next
                fast = fast.next.next
        
        # slow is pointing to the middle
        node = TreeNode(slow.val)

        # cut the list in half, without the middle element
        if prev_slow: 
            prev_slow.next = None
            node.left = self.sortedListToBST(head)
            node.right = self.sortedListToBST(slow.next)

        return node
