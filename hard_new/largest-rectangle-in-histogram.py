class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # https://leetcode.com/problems/largest-rectangle-in-histogram/?envType=study-plan-v2&envId=top-100-liked
        # monotonic increasing stack O(n) since we add and pop every element once
        # same thing as the commented solution bellow but a bit cleaner
        stack, maxArea, heights = [], 0, [0] + heights + [0]
        
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] >= heights[i]:
                start, height = stack.pop()
                maxArea = max(maxArea, (i-start) * height)
            stack.append((start, heights[i]))

        return maxArea

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         # https://leetcode.com/problems/largest-rectangle-in-histogram/?envType=study-plan-v2&envId=top-100-liked
#         # monotonic increasing stack O(n) since we add and pop every element once

#         stack = []
#         maxArea = 0
#         heights = [0] + heights + [0]

#         for i in range(len(heights)):
#             start = i
#             minHeight = stack[-1][1] if stack else None
#             while stack and stack[-1][1] >= heights[i]:
#                 start, height = stack.pop()
#                 # minHeight = min(minHeight, height)
#                 minHeight = height
#                 area = (i-start) * minHeight
#                 maxArea = max(maxArea, area)

#             stack.append((start, heights[i]))

#             # area = (i-start+1) * heights[i]
#             # maxArea = max(maxArea, area)
        
#         return maxArea