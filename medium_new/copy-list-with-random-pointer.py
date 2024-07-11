"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # https://leetcode.com/problems/copy-list-with-random-pointer/?envType=study-plan-v2&envId=top-interview-150
        # time complexity O(n)
        # an object can be a key of a harshtable ... i didnt know that. We till use that here.
        
        node_nodecopy = {None: None}
        def copyRandomList(head): 
            # if does not handle the random pointer
            if not head:
                return None
            head_copy = Node(head.val)
            next_copy = copyRandomList(head.next)
            head_copy.next = next_copy
            node_nodecopy[head] = head_copy
            return head_copy
        
        # creates a copy of the linked list and a harshtable with the pairs{node:node_copy}, but not the random pointers
        head_copy = copyRandomList(head) 

        # lets handdle the random pointers. For that we will use the harshtable
        node = head
        node_copy = head_copy
        while node:
            node_copy.random = node_nodecopy[node.random]

            node = node.next
            node_copy = node_copy.next

        return head_copy



