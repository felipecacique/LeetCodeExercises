class WordDictionary:
    # https://leetcode.com/problems/design-add-and-search-words-data-structure/?envType=study-plan-v2&envId=top-interview-150
    # based on implement-trie-prefix-tree's solution
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        
        cur = self.root

        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        
        cur['*'] = ''

    def search(self, word: str) -> bool:
        
        cur = self.root
        curs = [cur]

        for letter in word:
            newCurs = []
            for cur in curs:
                if letter == ".":  # iterate over all letters, and create many paths
                    for l in cur:
                        newCurs.append(cur[l])
                else:    
                    if letter in cur:
                        newCurs.append(cur[letter])
            curs = newCurs
            if not curs: return False

        for cur in curs:
            if '*' in cur: return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)