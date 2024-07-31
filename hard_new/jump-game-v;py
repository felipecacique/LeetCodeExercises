class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        def Solution1():
            # time O(n*d + nlogn)
            # Start from the smallest height to the top in a bottom up approach. 
            # We can only opdate the number of steps for a given ith if its is in increasing sequence, only k element to the right and k to the left
            heightIndex = sorted([(h, i) for i, h in enumerate(arr)])
            steps = [1] * len(arr)
            output = 1
            for h, i in heightIndex:
                lastHeight = h
                # moving d steps from the smalest height to right 
                for j in range(i+1, min(i+d+1, len(arr))):
                    heightRight = arr[j]
                    if heightRight > lastHeight:
                        steps[j] = max(steps[j], steps[i]+1) # the solution that is already there, or the solution coming from i
                        lastHeight = heightRight
                        output = max(output, steps[j])
                    
                lastHeight = h
                # moving d steps from the smalest height to left 
                for j in range(i-1, max(0, i-d)-1, -1):
                    heightLeft = arr[j]
                    if heightLeft > lastHeight:
                        steps[j] = max(steps[j], steps[i]+1)
                        lastHeight = heightLeft
                        output = max(output, steps[j])

            return output
        
        return Solution1()