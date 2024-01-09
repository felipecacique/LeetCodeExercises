# https://leetcode.com/problems/container-with-most-water/submissions/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # approach similar to sum of 2 iteratively, with pointers to the left and right of the array. We calculate the area between left and right. Then we can either move left+1 or right-1. But notice that if right's height is smaller than left's height, then we already have the max volume in which the right point is in. To see that we can just magining moving the left+1. We will never increase the height of the pool, since the height is limited by the right's height, but as e do left+1, we wimm be decreasing the width, and so the volume. Because of that, since right is smaller than left, we must move right-1. We do this untill left > right, storing the max computed volume. Time O(n)

        left = 0
        right = len(height) - 1

        max_volume = 0

        while left < right:
            
            volume = min(height[left], height[right]) * (right - left)

            max_volume = max(max_volume, volume)

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        return max_volume