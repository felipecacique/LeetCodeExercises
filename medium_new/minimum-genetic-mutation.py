class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # https://leetcode.com/problems/minimum-genetic-mutation/?envType=study-plan-v2&envId=top-interview-150
        # bfs, expands level by level, and each level represents the number of mutatios. As soon we get to the end gene, we have our min number of mutations needed
        from collections import deque
        queue = deque()
        seen = set()
        bankSet = set(bank)
        
        geneChars = ['A', 'C', 'G', 'T']

        queue.append((startGene,0)) 
        while queue:
            gene, n = queue.popleft() # n is the number of mutations so far
            
            if gene == endGene:
                return n

            for i in range(len(gene)):  # crete the mutation for every position of the gene
                for geneChar in geneChars:
                    if geneChar != gene[i]:
                        newGene = gene[:] # create a copy
                        newGene = list(newGene)
                        newGene[i] = geneChar # mutate the gene
                        newGene = "".join(newGene)
                        if newGene in bankSet and newGene not in seen:
                            queue.append((newGene,n+1))
                            seen.add(newGene)

        return -1