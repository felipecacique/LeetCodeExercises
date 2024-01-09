# https://leetcode.com/problems/reverse-linked-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution1: can we use recursion for this? we travel the list untill the end, a post order, and when get to the end, it will return the lasts node, then now we point the last node to the node before it. The recustion func will the return the reversed array. time O(n)

        def Solution1(head):
            newHead = [None]

            def dfs(node):
                if not node:
                    return None  # got to the end of the list

                node_next = dfs(node.next)  # return the next node

                node.next = None  # it will prevent a cycle that would happen in the last node of our reversed list. With this line, we make out çast node point to None, instead of pointing to the node before.

                if (
                    node_next == None
                ):  # got to the end of the list, so the current node is our last node
                    newHead[
                        0
                    ] = node  # holds a pointer to the head of the reversed list

                else:
                    node_next.next = node  # point the next node to the node before

                return node

            dfs(head)

            return newHead[0]

        return Solution1(head)
