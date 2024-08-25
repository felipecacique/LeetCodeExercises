class Solution:
    def countPairs(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/count-almost-equal-pairs-i/description/
        # O(nlogn + largestNumDigits**2)
        count = 0
        harsh = {}
        nums = sorted(nums)
        for num in nums:

            seen = set()
            numStr = list(str(num))
            if num in harsh:
                count += harsh[num]
                seen.add(num)
            for i in range(len(numStr)):
                for j in range(i+1, len(numStr)):
                    numStr[i], numStr[j] = numStr[j], numStr[i]
                    swiped = int("".join(numStr))
                    if swiped in harsh and not swiped in seen:
                        count += harsh[swiped]
                        seen.add(swiped)

                    numStr[i], numStr[j] = numStr[j], numStr[i]

            harsh[num] = harsh.get(num, 0) + 1
        
        return count