class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # https://leetcode.com/problems/concatenated-words/

        def isConcatenatedWord(word, wordInit):
            # if word == "": # reached the end of word, so the word at index idx is a concatenated word
            #     return True
            
            # lets check if we already know the solution in memo first, intead of calling the function again
            if word in memo:
                return memo[word]

            for i in range(len(word)):
                wordLeft, wordRight = word[:i+1], word[i+1:]
                if wordLeft in wordsSet and wordLeft != wordInit:
                    # we found a concatenated word that is word[:i+1]. Lest remove it call the isConcatenatedWord for the remaining
                    if isConcatenatedWord(wordRight, wordInit) == True:
                        memo[wordRight] = True
                        return True
                    else:
                        memo[wordRight] = False
            return False

        # We need to check the smallest len words first
        # wordsLen = [(len(word), word) for word in words]
        # wordsLen.sort()
        # wordsSorted = [wordLen[1] for wordLen in wordsLen]
        wordsSet = set(words)
        ans = []
        memo = {}
        words.sort(key = len)

        # For each word, check if it is a cancatenated word
        for word in words:
            if isConcatenatedWord(word, word):
                ans.append(word)
            memo[word] = True

        return ans