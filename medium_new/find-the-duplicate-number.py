class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-the-duplicate-number/?envType=study-plan-v2&envId=top-100-liked
        # s = set()
        # for num in nums:
        #     if num in s: return num
        #     s.add(num)
        
        # got the solution from https://www.youtube.com/watch?v=_n5MR8IxR6c. The idea is finding the cycle in a linked list. But i didnt understand very well this technic
        # Start a fast and slow pointer untill they meet
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # As soon as hey meet, move both pointers at same speed untill they meet again
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow