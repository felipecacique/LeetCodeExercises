# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #https://leetcode.com/problems/binary-search-tree-iterator/?envType=study-plan-v2&envId=top-interview-150
    # inspired by the leetcode solution 
    
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        curr = self.stack.pop()
        node = curr.right
        while node:
            self.stack.append(node)
            node = node.left
        return curr.val

    def hasNext(self) -> bool:
        return self.stack != []

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()




# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.root = root
#         dummy = TreeNode(-1)
#         dummy.left = root
#         self.queue = [root]
#         self.lastPop = root
#         self.hasNextCount = 0 #1 if root and root.right else 0
#         self.seen = set()
#         self.cach = 0
#         self.started = False
#         self.asd = False

#     def next(self) -> int:
#         # Implementing a depth first search with in order traversal using queue
#         # self.asd = False
#         for node in self.queue:
#             if node and node.right:
#                 self.asd = True

#         self.started = True
#         if self.cach == 1:
#             self.hasNextCount -= 1
#             self.cach = 0

#         while self.queue:
#             # print(self.queue[-1].val if self.queue[-1] else None)
#             node = self.queue[-1]
#             if not node: 
#                 self.queue.pop()
#                 continue
#             if node.right and not node.val in self.seen:
#                 self.hasNextCount += 1
#                 self.seen.add(node.val)
#             if not node.left and not node.right: 
#                 val = node.val
#                 print(val,self.hasNextCount)
#                 self.lastPop = self.queue.pop()
#                 break
#             if node.left: 
#                 self.queue.append(node.left)
#                 node.left = None # already appended in the queue
#                 continue
#             if node.right:
#                 # right before going to the right branch, we must process the value (in-order)
#                 val = node.val
#                 self.lastPop = self.queue.pop()
#                 self.queue.append(node.right)
#                 # self.hasNextCount -= 1
#                 self.cach = 1
#                 break
#         print(val, self.hasNextCount, "asdas")
#         return val

#     def hasNext(self) -> bool:
#         # return len(self.queue) > 0 and self.queue[-1] and self.queue[-1].right
#         # return self.lastPop and self.lastPop.right

#         # if self.started == False and self.root: return True
#         # return self.hasNextCount > 0
#         # return self.asd
#         for node in self.queue:
#             if node and node.right:
#                 return True
#         return False

        


# # Your BSTIterator object will be instantiated and called as such:
# # obj = BSTIterator(root)
# # param_1 = obj.next()
# # param_2 = obj.hasNext()