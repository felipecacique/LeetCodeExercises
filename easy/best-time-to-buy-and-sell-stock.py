# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1: Do 2 for loops, summing up the pairs and storing the ith pairs in which the sum is greatter. time O(n^2) space O(1)

        # Solution 2: we can do better. Lets cretae a new table with the variations, where diff[i] = prices[i+1] - prices[i]. Now our problem resumes in finding the subsequence with the greattest sum (maximum subarray problem). We can try to use hash table and dinamic programming.
        # The idea will be, lets imagine we are in the ith position. We have the biggest local sequence before ith. When adding the ith element to the sequence, we have 2 options. Or we add it to the current local sequence, or we start counting a new sequence. So, we must choose the one that is greatter.
        # The question is whether to add the ith element to the previous sequence or start a new sequence from ith. If adding the ith to the previous sequence is greatter than starting a new sequence, then we add it to previous, otherwise we start a new sequence. Finally we get the max value within the sequence sizes list.

        def Solution2():
            # maxSub(i+1) = max(maxSub[i], list[i] + list[i+1])
            # where maxSub is the biggest local sequence before ith in which includes ith. Note that this does not mean that maxSub is the biggest subsequence.

            if len(prices) == 0:
                return 0
            if len(prices) == 1:
                return 0

            diff = [
                prices[i] - prices[i - 1] for i in range(1, len(prices))
            ]  # create an array with the price variations

            sequenceSum = [
                0
            ]  # holds the sum of the local sequence (biggest sequence sum that includes ith)
            for i in range(0, len(diff)):
                sequenceSum.append(max(sequenceSum[-1] + diff[i], diff[i]))

            return max(sequenceSum)

        return Solution2()
