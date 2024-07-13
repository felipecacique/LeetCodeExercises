class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
        # [4, 3, 3, 2, 2]
        # time complexity O(n)

        arr = [0] + [0] * len(citations)
        for citation in citations:
            arr[min(citation, len(arr)-1)] += 1

        count = 0
        for i in range(len(arr)-1, -1, -1):
            count += arr[i]
            if count >= i:
                return i
