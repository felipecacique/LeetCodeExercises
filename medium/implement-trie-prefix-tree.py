# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
# i've got the solution from https://leetcode.com/problems/implement-trie-prefix-tree/solutions/3180933/solution/


class Trie:
    def __init__(self):
        self.root = {}  # structure of dictionary of dictionaries to represent the trie

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:  # move through this structure
            if not letter in cur:
                cur[
                    letter
                ] = (
                    {}
                )  # add the letter as keys, and the item is a new empty dict that will be filed with the sulfix worlds
            cur = cur[letter]

        cur["*"] = ""  # mark that the word has finished

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if not letter in cur:
                return False
            cur = cur[letter]

        return (
            "*" in cur
        )  # check if the word has finished. Notice that cur may have other words as well

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if not letter in cur:
                return False
            cur = cur[letter]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
