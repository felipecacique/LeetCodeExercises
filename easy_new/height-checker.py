class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # https://leetcode.com/problems/height-checker/
        count = 0
        expected = sorted(heights)
        for i in range(len(heights)):
            count += expected[i] != heights[i] 
        return count