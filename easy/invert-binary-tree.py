# https://leetcode.com/problems/invert-binary-tree/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # We can do a breath-first search (or depth-first search) travel and as soon we reach a node, we invert the pointers from left to right. We can use a queue (FIFO) and an iterative approach for the BFS. And we can use recursion for the DFS.

        # Solution using the DFS recursivelly. time O(n) space O(1)
        def Solution1(root):
            def dfs(node):
                # stop condition
                if node == None:
                    return

                # invert
                aux = node.left
                node.left = node.right
                node.right = aux

                dfs(node.left)
                dfs(node.right)

                return

            dfs(root)

            return root

        # Solution using the BFS recursivelly. time O(n) space O(n)
        def Solution2(root):
            def bfs(root):
                from queue import Queue

                q = Queue()

                q.put(root)

                while not (q.empty()):
                    # get node
                    node = q.get()
                    if node != None:
                        # invert
                        aux = node.left
                        node.left = node.right
                        node.right = aux
                        # add nodes to queue
                        q.put(node.left)
                        q.put(node.right)

                return

            bfs(root)

            return root

        return Solution1(root)
