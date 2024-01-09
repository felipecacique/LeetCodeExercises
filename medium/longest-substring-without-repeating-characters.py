# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Solution1: Lets try using the same approach for the problem "find max subsequence in array", but instead of computing the largest subsequence by the sum of its values, we will comput it by the ammout of distinct characters, something like thta ....  We will iterate over all char. The hashtable seen will hold the char of the subsequence. We keep adding char to it, until we find a char that is already in it. Then we have 2 options: Since c is alredy in our subsequence, we can either stop our subsequence there, and return its size, or que can add the new c, and remove the previous c from seen. We will always go for the second option, since we alredy have the size of the largest sequence so far, so have nothing to lose by going forward with this process, only the risk of finding a larger subsequence. Note that we also need to remove all the characters that appeared before the old c. Luckly we are also saving in the harshtable the id of the char, so that que can iterate s backwards from the position of the old c, and remove all characters that is in s from 'seen', untill the beggining of that subsequence. Then we update the variable to point to the start of the new subarray.time O(n) - we iterate over all char, and in the backwards part, we never remove from seen an element of a given id twice, since we are always updating the sequence_start to the start of the new sequence. And we only move backwards until this point.

        # Solution2: Lets try using divide and conquer, plus dinamic programing such as the staicase steps. When mergin the 2 subproblems, we will have the rule that we can only merge them if the longest sequence in the very right of the left problem can be merged with the longest subsequence in the very left of the right problem. Example: left = [x1, x2, x3, x4]  and right = [y1, y2, y3, y4]. We will always store the longest subsequence from right and lefts of the subproblems (in a harshtable), and its size.  We will look to the mergin point that is the variable x4 and y1. To be more precise, que eull look to the largest subsequence that x4 belongs (sequence_x4), and the one that y1 belongs (sequence_y1). We get the smallest one and for all of its elements, we check if it someone is also in the other side. If not, we  can merge them. Ops, this solution WILL NOT WORK, because both subproblems are not independent .....

        def Solution0(s):
            # travel the string twice, always checking if the charactar has already appeared in the sequence (harshtable)
            # O(s^2)
            seen = set()
            count = 0
            max_count = 0
            for i in range(0, len(s)):
                for c in s[i:]:
                    if not c in seen:
                        seen.add(c)
                        count += 1
                        max_count = max(max_count, count)
                    else:
                        seen = set()
                        count = 0
                        break

            return max_count

        def Solution1(s):
            # O(n)

            seen = {}  # holds the sequence values and its id in  the original string s
            count = 0
            max_count = 0
            sequence_start = 0
            for i in range(0, len(s)):
                c = s[i]
                if not c in seen:
                    seen[c] = i  # add new char to the sequence
                    count += 1
                else:
                    # remove the old c
                    old_char_pos = seen[c]  # gets the position of the old c in s
                    j = old_char_pos
                    while j >= sequence_start:
                        # remove all char before j from the hashtable
                        char_to_remove = s[j]
                        if (
                            not char_to_remove in seen
                        ):  # we moved backwards until we have found a char that does not belong to the sequence. Then we can just stop the removing process.
                            break
                        del seen[char_to_remove]
                        count -= 1
                        j -= 1
                    # points to the new c position
                    seen[c] = i  # add the new c
                    count += 1
                    sequence_start = (
                        old_char_pos + 1
                    )  # the new sequence starts from the next char to the j position

                max_count = max(max_count, count)

            return max_count

        return Solution1(s)
