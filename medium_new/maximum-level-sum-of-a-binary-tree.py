# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75
        max_sum = float('-inf')
        max_level = 0
        current_level = 1
        from collections import deque
        queue = deque([root])
        while queue:
            level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val

                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1
        return max_level

# works but a bit slow.The solution above is the same thing, but more optimized based on a submission's solution
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
#         levelSum = {}
#         from collections import deque
#         queue = deque([(root, 1)])
#         while queue:
#             node, level = queue.popleft()
#             levelSum[level] = levelSum.get(level, 0) + node.val
#             if node.left: queue.append((node.left, level+1))
#             if node.right: queue.append((node.right, level+1))
        
#         sumLevelList = []
#         for level, total in levelSum.items():
#             sumLevelList.append((-total,level))
#         sumLevelList.sort()

#         return sumLevelList[0][1]