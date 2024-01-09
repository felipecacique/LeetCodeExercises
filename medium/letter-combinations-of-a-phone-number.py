# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "": 
            return []

        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = ['']

        for digit in digits:

            new_combs = []
            for c in m[digit]:
                for comb in combinations:
                    new_comb = comb + c
                    new_combs.append(new_comb)
            
            combinations = new_combs
        
        return combinations

