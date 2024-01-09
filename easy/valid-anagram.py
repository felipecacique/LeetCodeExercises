# https://leetcode.com/problems/valid-anagram/submissions/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1: 2 fors. For each letter in s we chech if it appears in the t, and flag it. We might compare all pairs of letter between both string. time O(n^2) space O(n)

        # Solution 2: Lets create a frequency table. It will be a harsh table where the keys are the letters and the item are the letter count. In this way we can iterate the second string, and for each second string letter, we check if it exists in the harsh table. Then we must decreate the count by 1. It will be an anagram if for each letter in the second list we find its correspondent in the harsh table. And also the harsh count must be zero for all keys, which means that all keys (char from the first array) appeared in the second string the same in the exact same quantity. time O(n+m) space O(n)

        def Solution1():
            lettersHarsh = {}

            for letter in s:
                if not (letter in lettersHarsh):
                    lettersHarsh[letter] = 0

                lettersHarsh[
                    letter
                ] += 1  # we count how many times this letter appeared in s

            for letter in t:
                if not (letter in lettersHarsh):
                    return False
                else:
                    lettersHarsh[letter] -= 1
                    if (
                        lettersHarsh[letter] < 0
                    ):  # the letter apeared more time in t than in s
                        return False

            for (
                letter,
                count,
            ) in lettersHarsh.items():  # check if count for all keys is 0
                if count != 0:
                    return False

            return True

        return Solution1()
