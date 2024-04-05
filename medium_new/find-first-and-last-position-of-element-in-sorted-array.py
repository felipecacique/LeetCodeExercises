class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150
        
        def Solution1():
            # do binary search to find target. Then do 2 binary searches. 1 to the left to find the transition (a num in the left that is not target and a number in the right that is the target) which is the start. Do the same to fing the end.
            a = 0
            b = len(nums) - 1
            start, end = -1, -1
            while a <= b:
                middle = (b + a)//2
                if nums[middle] > target: b = middle - 1
                elif nums[middle] < target: a = middle + 1
                else: # nums[middle] == target:

                    # we found the target
                    b_aux = b

                    # do a bs in the left side to find start, searching for the transition
                    b = middle
                    while a <= b:
                        middle = (b + a)//2
                        if middle == 0 and nums[middle] == target or nums[middle] == target and nums[middle-1] != target:
                            start = middle
                            break
                        elif nums[middle] > target: b = middle - 1
                        elif nums[middle] < target: a = middle + 1
                        else: b = middle - 1

                    # do a bs in the right side to find end, searching for the transition
                    b = b_aux
                    a = middle
                    while a <= b:
                        middle = (b + a)//2
                        if middle == len(nums) -1 and nums[middle] == target or nums[middle] == target and nums[middle+1] != target:
                            end = middle
                            break
                        elif nums[middle] > target: b = middle - 1
                        elif nums[middle] < target: a = middle + 1
                        else: a = middle + 1

                    break
            
            return [start,end]

        def Solution2():
            # a bit faster than solution 1 and cleaner, more simple. Inspired in one of the sobmissions' solution
            a = 0
            b = len(nums) - 1
            start, end = -1, -1
            while a <= b:
                middle = (b + a)//2
                if nums[middle] > target: b = middle - 1
                elif nums[middle] < target: a = middle + 1
                else:
                    start = middle
                    b = middle - 1

            a = 0 if start == -1 else start
            b = len(nums) - 1
            while a <= b:
                middle = (b + a)//2
                if nums[middle] > target: b = middle - 1
                elif nums[middle] < target: a = middle + 1
                else:
                    end = middle
                    a = middle + 1
            
            return [start,end]


        return Solution2()
                