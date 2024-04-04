class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
        
        anagrams = {}

        for s in strs:
            key = tuple(sorted(s))
            anagrams[key]  = anagrams.get(key, []) + [s]
        
        anagrams = [anagram for key, anagram in anagrams.items()]

        return anagrams