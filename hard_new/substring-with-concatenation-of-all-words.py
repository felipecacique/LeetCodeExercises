class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150
        # time complexity (wordSize*len(s))
        output = set()
        wordSize = len(words[0])
        n = len(words)
        permutSize = wordSize* n
        
        for left in range(wordSize):
            left = left
            right = left
            wordsIncluding = {} # it is a counter
            wordsNotIncluding = {} # it is a counter
            wordsWindow = {} # it is a counter
            from collections import deque
            queue = deque()
            wordsIncludingTotal = 0

            for w in words:
                wordsIncluding[w] = 0
                wordsNotIncluding[w] = wordsNotIncluding.get(w, 0) + 1

            while right + wordSize <= len(s):
                
                if right - left >= permutSize:
                    # remove the left word
                    w = s[left:left+wordSize]
                    queue.popleft()
                    left += wordSize
                    wordsWindow[w] = wordsWindow.get(w, 0) - 1

                    if  w in wordsIncluding and wordsIncluding[w] > 0 and wordsWindow[w] < wordsIncluding[w]: # get the word from the wordsIncluding dict to the wordNotIncluding
                        wordsNotIncluding[w] = wordsNotIncluding[w] + 1
                        wordsIncluding[w] = wordsIncluding[w] - 1
                        wordsIncludingTotal -= 1

                w = s[right:right+wordSize]
                if w in wordsNotIncluding and wordsNotIncluding[w] > 0: # get the word from the wordsNotIncluding dict to the wordIncluding
                    wordsNotIncluding[w] = wordsNotIncluding[w] - 1
                    wordsIncluding[w] = wordsIncluding[w] + 1
                    wordsIncludingTotal += 1

                wordsWindow[w] = wordsWindow.get(w, 0) + 1
                queue.append(w)
                right += wordSize

                if wordsIncludingTotal >= n:
                    output.add(left)
                
        return output