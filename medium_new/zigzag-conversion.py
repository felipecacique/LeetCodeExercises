class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # p->      <-I->     <-N->
        # time complexity O(n)

        def Solution1():
            # there is a pattern in which you find the top letters and then get the left of it and the rigtht of it. And repeat the process
            # Get the start letters
            output = ""
            seen = set()
            n = len(s)
            from collections import deque
            sequence = deque()
            for i in range(n):
                idx = i*(2*numRows-2)
                if idx >= n: break
                if not idx in seen: 
                    sequence.append(idx)
                    seen.add(idx)

            if not sequence[-1] +(2*numRows-2) in seen:
                sequence.append(sequence[-1] +(2*numRows-2)) # add an extra position

            # Move in the sequence of the starting points, to the left and to the right, doing zig zag
            while sequence:
                idx = sequence.popleft()
                if idx<n: output += s[idx]
                if idx - 1 >= 0 and idx - 1 not in seen:
                    sequence.append(idx-1)
                    seen.add(idx-1)
                if idx + 1 < n and idx + 1 not in seen:
                    sequence.append(idx+1)
                    seen.add(idx+1)
            return output

        def Solution2():
            # faster. It was based on a solution from submissions
            if numRows == 1: 
                return s

            going_down = False
            word = [""] * numRows
            row = 0
            for c in s:
                word[row] += c

                if row == 0 or row == numRows - 1:
                    going_down = not going_down
                row += 1 if going_down else -1
            
            return "".join(word)


        return Solution2()

