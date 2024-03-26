class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

        highest = 0
        altitude = 0
        for g in gain:
            altitude += g
            highest = max(highest, altitude)

        return highest 
        