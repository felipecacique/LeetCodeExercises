class Solution:
    def canWinNim(self, n: int) -> bool:
        # https://leetcode.com/problems/nim-game/
        # 1 stone - 1 win
        # 2 - remove  2 stanes - 1 win
        # 3 remove 3 - i win
        # 4 - he wins
        # 5 - i take one, and go ot problem 4- i win// i take 2 or 1 // he wins
        # 6 - i take one
        
        # 0, 1, 2, 3, 4*, 5 ,6 ,7 ,8* ,9, 10
        # the player who starts in multiples of 4 will lose
        
        return False if n % 4 == 0 else True