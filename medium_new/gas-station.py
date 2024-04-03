class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [2 2 2 -3 2 2 -1 -9 -1]
        # [2 4 6  3 6 8  7 -2 -3]
        # use pointers

        # https://leetcode.com/problems/gas-station/?envType=study-plan-v2&envId=top-interview-150

        if len(gas) == 1:
            if gas[0] >= cost[0]: return 0
            else: -1
        
        if sum(gas) < sum(cost):
            return -1

        start, end, tank, count = 0, 1, gas[0], 0
        while 1:
            if start == end-1:
                count += 1
                if count == 2: break

            # can i go from start to end?
            if tank >= cost[end-1]:
                # we can move from start to end
                tank += gas[end] - cost[end-1]
                if end == start: return start
                end += 1 # points to the right station
                if end >= len(gas): end = 0
            else:
                # we cannot go from start to end. So e must have started before 
                start -= 1
                if start < 0: start = len(gas) - 1
                tank += gas[start] - cost[start] # if we have started in start - 1, this is our tank when reaching end
        return -1
