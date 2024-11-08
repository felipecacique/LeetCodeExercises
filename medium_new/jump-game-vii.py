class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # https://leetcode.com/problems/jump-game-vii/
        # check if the j can be reached by the window on the left
        # all positions within the window can reach j. So if there is a "0" in the window, that is reachable, then j can be reached. If we can reach the last "0" then we return true
        # we will use dp with cum sum t okeep track of the amount of reachable "0"s with the sliding window. We could also use a monotonic queue instead of a sliding window
        # time O(n) space O(n)

        if s[-1] != "0": return False

        reachable = [False] * len(s)
        reachable[0] = True
        countReachable = 0

        for j, c in enumerate(s):
            window_start = j - maxJump
            window_end = j - minJump

            if window_start - 1 >= 0 and reachable[window_start - 1] == True: countReachable -= 1
            if window_end >= 0 and reachable[window_end] == True: countReachable += 1

            if j > 0 and c == "0" and countReachable > 0:
                reachable[j] = True

        return reachable[-1]
            

