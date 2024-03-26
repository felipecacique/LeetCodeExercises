class Solution:
    def reverseVowels(self, s: str) -> str:
        # https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

        s_list = [l for l in s]
        vowels = set(['a', 'e', 'i', 'o','u'])

        a = 0
        b = len(s) - 1

        while a < b:
            if s_list[a].lower() in vowels:
                while b > a:
                    if s_list[b].lower() in vowels:
                        s_list[a], s_list[b] = s_list[b], s_list[a]
                        b -= 1
                        break
                    b -= 1
            a += 1
        
        return "".join(s_list)