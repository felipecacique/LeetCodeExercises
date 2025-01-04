class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # https://leetcode.com/problems/maximum-units-on-a-truck/submissions/1497839450/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # O(n)
        boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse=True)
        ans = 0
        for i in range(len(boxTypes)):
            if truckSize - boxTypes[i][0] <= 0:
                ans += truckSize * boxTypes[i][1]
                return ans
            truckSize -= boxTypes[i][0]
            ans += boxTypes[i][0] * boxTypes[i][1]
        return ans
