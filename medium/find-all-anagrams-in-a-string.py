# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # solution 1 - put all anagram of p in a dictioary or set, and then check in s if we have that anagram, for each s[i:anagram_size].
        # solution 2 - put all words from p in a dict, with its count. Then Go though s, word by word, and drop it from the dict in sequence. If count is all 0, then we have found one anagram.
        
        # implementing solution 2
        
        # counts = {}

        # for w in p:
        #     if not w in counts:
        #         counts[w] = 1
        #     else:
        #         counts[w] += 1

        # anagrams_index =[]
        # n = len(s)
        # m = len(p)
        # for i in range(0, n):
        #     total_count = m
        #     counts_ = counts.copy()
            
        #     for j in range(i, i+m):
        #         if j >= n:
        #             break
        #         if not s[j] in counts_:
        #             break
        #         else: # s[i] in w
        #             if  counts_[s[j]] > 0:
        #                 counts_[s[j]] -= 1
        #                 total_count -= 1
        #             else:
        #                 break
                
        #         if total_count == 0:
        #             # found an anagram starting in i and finishing in j
        #             anagrams_index.append(i)

        


        # we did a great optimization here. Instead of recomputing the counts for s, we do the count until it is "full", and then we add a new item, and then remove the last one, mantaining the total count constant. Then we compare if the counts2 (count for s from start to end) and counts (counts for p). If they are equual, then we have an anagram.
        counts = {}

        for w in p: # time O(m)
            if not w in counts:
                counts[w] = 1
            else:
                counts[w] += 1


        anagrams_index =[]
        n = len(s)
        m = len(p)
        counts2 = {}
        max_count = m
        count = 0

        for i in range(0, n):

            if not s[i] in counts2:
                counts2[s[i]] = 1
                count += 1
            else:
                counts2[s[i]] += 1
                count += 1
            
            if count > max_count: #we must maantain the size of the counts2 (ne number of itens of s that it is counting). If it is surpassed the limit, we must remode one item, actually the first item on left that was added to counts2 before. Its index is i-max_count. Notice that for every item we add, we  only have to operations that are addding one item to the dict, and removing one item. We do not need to recompute counts2 over and over again within this loop. It is a great optimization. Time O(1)

                counts2[s[i-max_count]] -= 1
                count -= 1
                if counts2[s[i-max_count]] == 0:
                    del counts2[s[i-max_count]]
           

            # # check if counts2 == counts for all keys. If if does, then we have an anagram starting in i-max_count+1
            # flag = True
            # for key, item in counts.items():
            #     if key in counts2:
            #         if counts2[key] == counts[key]:
            #             # flah = True
            #             pass
            #         else:
            #             flag = False
            #     else:
            #         flag = False
            #     # found an anagram starting in i-max_count+1 and finishing in i
            # if flag == True:
            if counts == counts2: # we can compare 2 dictionaries directly. It is faster. Time O(m)
                anagrams_index.append(i-max_count+1)


        # the total complexity in the wost case is time O(m*n), that is to compare dictionaries for each  element of s

        return anagrams_index




