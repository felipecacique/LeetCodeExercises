class Solution:
    def compress(self, chars: List[str]) -> int:
        # https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
        
        # 1 approach
        # chars = ["a","a","b","b","c","c","c"] time complexity O(n)
        # s = ['a2b2c3'] space O(n)

        # 2 approach
        # chars = ["a","2","b","2","c","3","d","d"] time complexity O(n) space O(1)

        j = 0
        groupLetter = ''
        groupCounter = 0
        groupCounterStr = ''
        # iterate over chars array
        for i in range(len(chars)):
            
            if chars[i] != groupLetter:
                groupLetter = chars[i]
                if groupCounter > 1:
                    # groupCounterStr = str(groupCounter)
                    for k in groupCounterStr:
                        j += 1
                groupCounter = 0

            groupCounter += 1

            if groupCounter == 1:
                chars[j] = groupLetter
                j += 1
            else:
                groupCounterStr = str(groupCounter)
                for k in range(len(groupCounterStr)):
                    chars[j+k] = groupCounterStr[k]
        
        if groupCounter > 1:
            groupCounterStr = str(groupCounter)
            return j+len(groupCounterStr)
        else:
            return j



        
