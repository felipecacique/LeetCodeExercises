class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=study-plan-v2&envId=leetcode-75
        res = []
        potions.sort()

        for spell in spells:
            lookUp = success / spell

            if lookUp > potions[-1]: # only to make a bit faster
                res.append(0)
                continue 

            # binary search
            l, r = 0, len(potions)
            while l < r:
                middle = (l + r) // 2
                if potions[middle] >= lookUp:
                    r = middle
                else:
                    l = middle + 1
            res.append(len(potions)-l)

        return res