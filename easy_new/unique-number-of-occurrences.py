class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75
        
        hashCount = {}
        for n in arr:
            hashCount[n] = hashCount.get(n,0) + 1
        
        setUnique = set()
        for num, count in hashCount.items():
            if count in setUnique:
                # the num count (ocurrences) is already in setUnique, so is not unique
                return False
            else:
                setUnique.add(count)
        return True