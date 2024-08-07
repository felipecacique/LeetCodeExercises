class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
        s = s.split(" ")
        mapCharWord= {}
        mapWordChar= {}
        if len(pattern) != len(s): return False
        for i in range(len(pattern)):
            char = pattern[i]
            word = s[i]
            if char not in mapCharWord: mapCharWord[char] = word
            if word not in mapWordChar: mapWordChar[word] = char

            if mapCharWord[char] != word or mapWordChar[word] != char: 
                # patterns does not mach
                return False
        return True

# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         # https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
#         s = s.split()
#         if len(pattern) != len(s):
#             return False
#         pattern_s = {}
#         s_pattern = {}
#         for i in range(len(pattern)):
#             if not pattern[i] in s_pattern and not s[i] in pattern_s:
#                 s_pattern[pattern[i]] = s[i]
#                 pattern_s[s[i]] = pattern[i]
#             else:
#                 if pattern[i] in s_pattern and s_pattern[pattern[i]] != s[i] or s[i] in pattern_s and pattern_s[s[i]] != pattern[i]:
#                     return False
#         return True
