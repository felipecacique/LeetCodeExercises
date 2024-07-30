class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # https://leetcode.com/problems/longest-absolute-file-path/submissions/1337858307/
        # O(n)
        
        longest = 0
        s = input.split("\n")
        lastLevelFolders = {-1:""}
        
        for names in s:
            names = names.split("\t")
            depth = len(names) - 1
            name = names[-1]
            newPath = lastLevelFolders[depth-1] + "/" + name
            lastLevelFolders[depth] = newPath
       
            if "." in name: longest = max(longest, len(newPath)-1)

        return longest
                