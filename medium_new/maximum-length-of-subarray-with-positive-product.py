class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # time O(n) space O(1)
        
        ans = 0
        countNeg1 = 0 # number of negative numbers of a subsequence after 0
        countNeg2 = 0 # number of negative numbers of a subsequence sequence after the first negative number
        i1, i2 = 0, 0
        flag = False

        for r in range(len(nums)):
            if nums[r] == 0: 
                countNeg1 = 0
                i1 = r + 1
                flag = False
                continue

            # product of subsequence with odd/even negative numbers
            if nums[r] < 0: countNeg1 += 1
            if countNeg1 % 2 == 0: # even negative numbers, so the product ir positive
                ans = max(ans, r - i1 + 1)


            # product of subsequence with even/odd negative numbers
            if flag:
                if nums[r] < 0: countNeg2 += 1
                if countNeg2 % 2 == 0: # even negative numbers, so the product ir positive
                    ans = max(ans, r - i2 + 1)
                continue

            if not flag and nums[r] < 0:
                countNeg2 = 0
                i2 = r + 1
                flag = True

        return ans



        # ans = 0
        # prod1 = 1 # prod of a subsequence after 0
        # prod2 = 1 # prod of a subsequence sequence after the first negative number
        # i1, i2 = 0, 0
        # flag = False

        # for r in range(len(nums)):
        #     if nums[r] == 0: 
        #         prod1 = 1
        #         i1 = r + 1
        #         flag = False
        #         continue

        #     # product of subsequence with odd/even negative numbers
        #     prod1 *= nums[r] 
        #     if prod1 > 0:
        #         ans = max(ans, r - i1 + 1)

        #     # product of subsequence with even/odd negative numbers
        #     if not flag and nums[r] < 0:
        #         prod2 = 1
        #         i2 = r + 1
        #         flag = True
        #         continue

        #     if flag:
        #         prod2 *= nums[r] 
        #         if prod2 > 0:
        #             ans = max(ans, r - i2 + 1)

        # return ans