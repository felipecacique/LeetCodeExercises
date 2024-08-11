class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        # https://leetcode.com/problems/snake-in-matrix/description/
        i = 0
        j = 0
        for c in commands:
            if c =="UP": j-=1
            elif c=="DOWN": j+= 1
            elif c == "LEFT": i-=1
            elif c == "RIGHT": i+=1
        
        return j * n + i