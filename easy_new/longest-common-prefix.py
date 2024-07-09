class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # common_prefix = ""
        # n = min([len(word) for word in strs])
        # for i in range(n):
        #     letters = set()
        #     for word in strs:
        #         letters.add(word[i])
        #     if len(letters) == 1:
        #         common_prefix += word[i] 
        #     else:
        #         return common_prefix
        # return common_prefix

        # complexity O(nlogn + m) where m is the size of the smallest word
        common_prefix = ""
        m = min([len(word) for word in strs])
        strs = sorted(strs)
        for i in range(m):
            word_start = strs[0]
            word_end = strs[-1]
            if word_start[i] == word_end[i]:
                common_prefix += word_start[i]
            else:
                return common_prefix
        return common_prefix