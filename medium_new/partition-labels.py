class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # https://leetcode.com/problems/partition-labels/?envType=study-plan-v2&envId=top-100-liked
        # time o(n) space o(n)
        
        from collections import Counter
        freq = Counter(s)
        sSet = set()
        partition = []
        output = []

        for char in s:
            partition.append(char)
            sSet.add(char)

            freq[char] -= 1
            if freq[char] == 0:
                sSet.remove(char)
            
            if not sSet:
                output.append(len(partition))
                partition = []
        
        return output