class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # https://leetcode.com/problems/subarray-sum-equals-k/?envType=study-plan-v2&envId=top-100-liked
        count = 0
        harsh = {0:1}
        prefixSum = [0]
        for num in nums:

            prefix = prefixSum[-1] + num

            if prefix - k in harsh:
                count += harsh[prefix - k]

            prefixSum.append(prefix)
            harsh[prefix] = harsh.get(prefix, 0) + 1

        return count
