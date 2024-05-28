class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # https://leetcode.com/problems/get-equal-substrings-within-budget/?envType=daily-question&envId=2024-05-28
        # use 2 ponters, left and right pointing to the substring. If we reach a cost greatter than maxCost, in odret to be able to add a new char (rightt = right+1) e must drop the left char of the string by (left+=1). So we will gerenate the substring that is max, and as we itereate we store the max length found 
        # O(n)

        # s = list(s.encode('ascii'))
        # t = list(t.encode('ascii'))
        maxLen = -1
        cost = 0
        left = 0
        right = 0
        n = len(s)

        while right < n:
            
            aux =  abs(ord(s[right]) - ord(t[right])) + cost
            if aux <= maxCost:
                cost = aux
                right += 1
                maxLen = max(maxLen, right-left)
            else:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

        return maxLen
    


# class Solution:
#     def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
#         # https://leetcode.com/problems/get-equal-substrings-within-budget/?envType=daily-question&envId=2024-05-28
#         # use 2 ponters, left and right pointing to the substring. If we reach a cost greatter than maxCost, in odret to be able to add a new char (rightt = right+1) e must drop the left char of the string by (left+=1). So we will gerenate the substring that is max, and as we itereate we store the max length found 
#         # O(n)

#         # s = list(s.encode('ascii'))
#         # t = list(t.encode('ascii'))
#         maxLen = -1
#         cost = 0
#         left = 0
#         right = 0
#         n = len(s)

#         for right in range(len(s)):

#             while abs(ord(s[right]) - ord(t[right])) + cost > maxCost:
#                 cost -= abs(ord(s[left]) - ord(t[left]))
#                 left += 1

#             cost = abs(ord(s[right]) - ord(t[right])) + cost
            
#             maxLen = max(maxLen, right - left + 1)

#         return maxLen