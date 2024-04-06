class Solution:
    def intToRoman(self, num: int) -> str:
        # https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
        
        def Solution1(num):
                
            roman_to_int = {1:'I', 5:'V', 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
            
            roman = ""
            for n in [1000, 500, 100, 50, 10, 5, 1]:
                while int(num / n) != 0:
                    roman = roman + roman_to_int[n]
                    num = num - n

            # now deal with wrong roman due to those 6 instances from the descrioption
            # there should never be more than 3 letters repeated. If we find "IIII" we replace it with a "IV"
            # we can use a stack
            # replacements = {"IIII": "IV", "VIIII": "IX", "XXXX": "XL", "LXXXX": "XC", "CCCC": "CD", "DCCCC": "CM"}
            replacements_reversed = {"IIII": "VI", "IIIIV": "XI", "XXXX": "LX", "XXXXL": "CX", "CCCC": "DC", "CCCCD": "MC"}
            roman = list(reversed(roman))
            for size in [5,4]:
                clean_roman = []
                for i in range(len(roman)):
                    clean_roman.append(roman[i])
                    if size == 4 and len(clean_roman) < 4: continue  
                    elif size == 5 and len(clean_roman) < 5:continue 
                    rom = "".join(clean_roman[-size:])
                    if rom in replacements_reversed:
                        for _ in range(size): 
                            clean_roman.pop() 
                        for c in replacements_reversed[rom]: 
                            clean_roman.append(c)
                roman = clean_roman

            clean_roman = reversed(clean_roman)

            return "".join(clean_roman)
            
        def Solution2(num):

            int_to_roman = {
                1: "I",
                5: "V",    4: "IV",
                10: "X",   9: "IX",
                50: "L",   40: "XL",
                100: "C",  90: "XC",
                500: "D",  400: "CD",
                1000: "M", 900: "CM",
            }

            roman = ""
            for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
                while int(num / n) != 0:
                    roman = roman + int_to_roman[n]
                    num = num - n

            return roman


        return Solution2(num)
