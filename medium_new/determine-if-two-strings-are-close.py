class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75
        # o(nlogn)
        
        if len(word1) != len(word2): return False

        # from collections import defaultdict
        # harsh1, harsh2 = defaultdict(int), defaultdict(int)
        # for w in word1: harsh1[w] += 1
        # for w in word2: harsh2[w] += 1

        from collections import Counter
        
        harsh1 = Counter(word1)
        harsh2 = Counter(word2)

        return sorted(harsh1.values()) == sorted(harsh2.values()) and set(harsh1.keys()) == set(harsh2.keys())

        # count_w1, count_w2 = defaultdict(int), defaultdict(int)
        # for w, count in harsh1.items(): count_w1[count] += 1
        # for w, count in harsh2.items(): count_w2[count] += 1

        # return count_w1 == count_w2 and set(harsh1.keys()) == set(harsh2.keys())
