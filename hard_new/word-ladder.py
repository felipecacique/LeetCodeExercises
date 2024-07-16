class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # https://leetcode.com/problems/word-ladder/?envType=study-plan-v2&envId=top-interview-150
        # bfs O(beginWord.length*26*n) => O(n)
        import string
        alphabet = list(string.ascii_lowercase)
        wordSet = set(wordList)
        if not endWord in wordSet: return 0
        from collections import deque
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            # print(queue)
            word, count = queue.popleft()
            if word == endWord:
                return count
            # Generate all of the possible s1 transformations of word (for every char, replace it for 26 english letters), and check if it is in the wordSet
            wordArr = list(word)
            for i in range(len(wordArr)):
                s1Arr = wordArr.copy()
                for c in alphabet:
                    s1Arr[i] = c
                    s1 = "".join(s1Arr)
                    if s1 in wordSet:
                        queue.append((s1, count+1))
                        wordSet.remove(s1)
        return 0