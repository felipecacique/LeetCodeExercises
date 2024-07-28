class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # https://leetcode.com/problems/1-bit-and-2-bit-characters/submissions/1336556608/
        # go greedy
        
        char = []
        for bit in bits:
            if char == [1,0] or char == [1,1] or char == [0]: char = []
            char.append(bit)
        return True if char == [0] else False