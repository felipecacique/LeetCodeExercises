class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/
        return ((ord(coordinate1[0]) - ord('a') + 1 + int(coordinate1[1])) % 2) == ((ord(coordinate2[0]) - ord('a') + 1 + int(coordinate2[1])) % 2)