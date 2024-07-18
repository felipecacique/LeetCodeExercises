class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # https://leetcode.com/problems/word-search-ii/?envType=study-plan-v2&envId=top-interview-150
        # lets add the words in a dictionary type of trie. Do a dfs on the trie and the board simultaneously, comparing the words. If they match, we keep traversing ...

        # Add the words in a trie
        root = {}
        for word in words:
            cur = root
            for letter in word:
                if not letter in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur['*']  = ''

        # This function delete_word_from_trie I got from a conde sample from submissions
        def delete_word_from_trie(t, word):
            if word:
                delete_word_from_trie(t[word[0]], word[1:])
                if not t[word[0]]:
                    del t[word[0]]
            else:
                del t["*"]

        # We will do a double dfs on the board and the trie simultaneously
        output = set()
        stack = []
        m, n = len(board), len(board[0])
        for j in range(m):
            for i in range(n):
                letter = board[j][i]
                if letter in root: 
                    stack.append((j,i,root[letter],letter, "")) # add the reference for the board and for the node in the trie
        
        seenGlobal = set() 

        while stack:
            j, i, cur, word, order = stack.pop()
            
            if order == "POST-ORDER":
                seenGlobal.remove((j,i))
                continue
            
            seenGlobal.add((j,i))

            # Before exploring the node, lets add it to the post order (necessary in order to remove visited from seen, like in a recursive implementation of dfs, without the need to make a copy of seen)
            stack.append((j, i, cur, word, "POST-ORDER")) # POST ORDER

            if "*" in cur: # we found the word
                output.add(word)
                delete_word_from_trie(root, word) # This function delete_word_from_trie I got from a conde sample from submissions
                                                  # By removing the found words, improves exponentially the speed, because we avoid repeating the same words again and again. This I got from the submissions code
                
            for jnext, inext in [(j-1,i), (j+1,i), (j,i-1), (j,i+1)]:
                if jnext >= 0 and inext >= 0 and jnext < m and inext < n: 
                    letter = board[jnext][inext]
                    wordNext = word+letter
                    if letter in cur and (jnext,inext) not in seenGlobal: # and wordNext not in output
                        stack.append((jnext,inext,cur[letter],wordNext, ""))
            
        return output

            
                