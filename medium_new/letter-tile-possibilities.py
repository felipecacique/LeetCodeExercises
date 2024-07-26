class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # https://leetcode.com/problems/letter-tile-possibilities/
        seqs = set() # store all the sequences
        seen = set() # seen indexes
        def dfs(seq):
            if len(seq) >= len(tiles): return
            for i, c in enumerate(tiles):
                if seq + c not in seqs and i not in seen:
                    seqs.add(seq + c)
                    seen.add(i)
                    dfs(seq + c)
                    seen.remove(i)
        dfs("")        
        return len(seqs)