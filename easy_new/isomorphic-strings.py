class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): return False

        mapping = {}
        mapping_inverse = {}

        for i, char in enumerate(t):
            char_map = s[i]
            if char in mapping:
                if mapping[char] != char_map:
                    return False
            elif char_map in mapping_inverse:
                if mapping_inverse[char_map] != char:
                    return False
            else:
                mapping[char] = char_map
                mapping_inverse[char_map] = char
        return True