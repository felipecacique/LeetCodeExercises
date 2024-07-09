class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # https://leetcode.com/problems/contains-duplicate-ii/submissions/1315382930/?envType=study-plan-v2&envId=top-interview-150
        window = set()
        for i in range(len(nums)):
            if nums[i] in window: return True
            window.add(nums[i])
            if len(window) > k: window.remove(nums[i-k])
        return False
            
            
