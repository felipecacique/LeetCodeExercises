class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # https://leetcode.com/problems/search-suggestions-system/?envType=study-plan-v2&envId=leetcode-75
        # products.sort()
        
        root = {}

        for product in products:
            cur = root
            for letter in product:
                if not letter in cur:
                    cur[letter] = {}
                cur = cur[letter]
            cur['*'] = ''
        
        output = []

        cur = root
        word = ""
        for letter in searchWord:
            if letter not in cur:
                break
            cur = cur[letter]
            word += letter
            
            # Do a dfs - go deph and get the word
            suggestions = []
            stack = [(cur,word)]
            while stack:
                cur2, word2 = stack.pop()
                if '*' in cur2:
                    suggestions.append(word2)
                    if len(suggestions) >= 3: break
                if cur2 == "": continue
                keys = sorted(cur2.keys())[:3]
                for key in reversed(keys):
                    stack.append((cur2[key],word2+key))
            output.append(suggestions)

        return output + [[]]*(len(searchWord) - len(word))