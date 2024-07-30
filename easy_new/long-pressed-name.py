class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # https://leetcode.com/problems/long-pressed-name/
        name += "."
        typed += "."
        i = 0
        prev_c = ""
        count = 0
        for c in name:
            while i < len(typed) and (prev_c == typed[i] or c == typed[i]):
                if c == typed[i]:
                    i += 1
                    count += 1
                    break
                i += 1
            prev_c = c
        return count == len(name)