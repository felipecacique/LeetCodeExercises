class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # https://leetcode.com/problems/prison-cells-after-n-days/
        # find the cycle, number of days in which a pattern repeats. Then in the for loop we use the remaining_cycle that is remaining_days = n % cycle
        initial = None
        cycle = None
        for j in range(n):
            aux = [0] * len(cells)
            if j == 1:
                initial = cells.copy() # we get from here because of the 1's that migh appear on the start and end of the cells. So we copy the array after we remove those 1's
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    aux[i] = 1
            cells = aux
            if j!=0 and tuple(cells) == tuple(initial):
                cycle = j  # the pattern repeats at every cycle 
                break

        if cycle:
            # repeat the process
            remaining_days = (n-1) % cycle
            for j in range(0,remaining_days):
                aux = [0] * len(cells)
                for i in range(1, len(cells)-1):
                    if cells[i-1] == cells[i+1]: 
                        aux[i] = 1
                cells = aux

        return cells