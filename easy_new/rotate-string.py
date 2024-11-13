class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # https://leetcode.com/problems/rotate-string/
        return s in goal+goal and len(s) == len(goal)