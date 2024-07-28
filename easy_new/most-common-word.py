class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # https://leetcode.com/problems/most-common-word/
        bannedSet = set()
        for b in banned:
            bannedSet.add(b.lower())
        
        paragraph = paragraph.lower()
        paragraphClean = ""
        for char in paragraph:
            if char.isalpha(): paragraphClean += char
            else: paragraphClean += " "
        paragraphList = paragraphClean.split()
        
        wordFreq = {}
        mostFreq = ""
        mostFreqCount = 0
        for word in paragraphList:
            if word not in bannedSet:
                wordFreq[word] = wordFreq.get(word, 0) + 1
                if wordFreq[word] > mostFreqCount:
                    mostFreqCount = wordFreq[word]
                    mostFreq = word

        return mostFreq