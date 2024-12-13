class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        # https://leetcode.com/problems/find-good-days-to-rob-the-bank/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # Time and space O(n)
        
        ans = []
        cumSumBefore = [0] * len(security)
        cumSumAfter = [0] * len(security)

        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                cumSumBefore[i] = cumSumBefore[i-1] + 1
            # else:
            #     cumSumBefore[i] = 0
        
        for i in range(len(security)-2, -1, -1):
            if security[i] <= security[i+1]:
                cumSumAfter[i] = cumSumAfter[i+1] + 1
            # else:
            #     cumSumAfter[i] = 0
        
        for i in range(len(cumSumBefore)):
            if cumSumBefore[i] >= time and cumSumAfter[i] >= time:
                ans.append(i)
        
        return ans