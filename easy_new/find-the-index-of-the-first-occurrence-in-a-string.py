class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle_size = len(needle)
        ans = -1
        for i in range(len(haystack)):
            if i + needle_size > len(haystack):
                break
            if haystack[i] == needle[0]:
                if haystack[i: i + needle_size] == needle:
                    ans = i
                    break
        return ans