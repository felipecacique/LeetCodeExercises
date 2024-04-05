class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def Solution1(nums,target):
            # brute solution is O(n^4). Our solution will be O(n^3). We will do brute force untill we reach two numbers, then use twoSum approach to solve for these last 2 numbers
            def twoSumIndex(nums,target,start):
                seen = {}
                pairs = []
                seen2 = set()
                for i in range(start,len(nums)):
                # for i in range(len(nums)-1,start-1,-1):
                    # if i-1>=start+1 and nums[i] == nums[i-1]: continue # to avoid duplicates
                    n = nums[i]
                    c = target - n
                    if c in seen:
                        for c_index in seen[c]:
                            # pairs.append([c_index,i]) # return the indexes of the numbers
                            output.add(tuple(sorted([nums[a], nums[b], nums[c_index], nums[i]])))
                    if n not in seen2:
                        seen[n] = seen.get(n,[]) + [i]
                        seen2.add(n) # to avoid duplicates
                return pairs

            nums = sorted(nums) # help us to remove duplicates
            output = set()
            memo = set()
            # go over all combinations
            prev_a = float(inf)
            for a in range(len(nums)):
                if a-1>=0 and nums[a] == nums[a-1]: continue # to avoid duplicates
                for b in range(a+1,len(nums)):
                    if b-1>=a+1 and nums[b] == nums[b-1]: continue # to avoid duplicates
                    # nums[a] + nums[b] + nums[c] + nums[d] = target
                    # nums[c] + nums[d] = target - nums[a] - nums[b] = target2sum 
                    target2sum  =  target - nums[a] - nums[b]
                    if (b+1,target2sum) not in memo: # check in a memo if we already have a solution for this problem
                        pairs = twoSumIndex(nums,target2sum,b+1) # apply the twoSum O(n)
                        memo.add((b+1,target2sum))
                        # if pairs:
                        #     for c, d in pairs:
                        #         output.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))

            return sorted(output)


        def Solution2(nums,target):
            # great solution!
            # O(n^4) in the worse situation (duplicates but we have already solve it) or O(n^2)??
            nums = sorted(nums) # help us to remove duplicates
            output = set()
            dp = {}
            for a in range(len(nums)):
                if a-1>=0 and nums[a] == nums[a-1]: continue # to avoid duplicates
                for b in range(a+1,len(nums)):
                    if b-1>=a+1 and nums[b] == nums[b-1]: continue # to avoid duplicates
                    sum_ab = nums[a] + nums[b]
                    dp[sum_ab] = dp.get(sum_ab, []) + [[a,b]]

            for c in range(len(nums)):
                for d in range(c+1,len(nums)):      
                    sum_ab  =  target - nums[c] - nums[d]
                    if sum_ab in dp:
                        for a, b in dp[sum_ab]:
                            if a!=c and a!=d and b!=d and b!=c:
                                output.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
            return output

        return Solution2(nums,target)

        


