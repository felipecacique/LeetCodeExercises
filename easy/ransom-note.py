# https://leetcode.com/problems/ransom-note/submissions/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # lets create a harsh table for store the frequency of the words in ransomNote. Then we iterate through the magazine, and each word in magazine that maches with a word in the hashtable, we decrease 1 in the frequency for that word. If the hashtable contains only zero in the count, then for each words in ransomNote we could find a match in the magazine and then we return true. time O(n+m) space = O(n)

        ransomNoteHarsh = {}
        totalLettersInNote = 0
        for letter in ransomNote:
            if not letter in ransomNoteHarsh:
                ransomNoteHarsh[letter] = 1
                totalLettersInNote += 1
            else:
                ransomNoteHarsh[letter] += 1
                totalLettersInNote += 1

        for letter in magazine:
            if letter in ransomNoteHarsh and ransomNoteHarsh[letter] > 0:
                ransomNoteHarsh[letter] -= 1
                totalLettersInNote -= 1
                if totalLettersInNote == 0:
                    return True

        return False
