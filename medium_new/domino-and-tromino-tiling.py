class Solution:
    def numTilings(self, n: int) -> int:
        # https://leetcode.com/problems/domino-and-tromino-tiling/?envType=study-plan-v2&envId=leetcode-75
        # My solution: lets add piece by piece, which leads to a new bords of size i+1 or i+2, depending on the piece. So we have to think of all possibilities in whicn the borad can end, and then add a new piece, and that will ginerate a board of size +1 that ends in a different way (status). We iterate this proccess of adding pieces.
        
        size = [{} for _ in range(n+2)]
        size[0] = {("complete"): 1} # "right_down_empty",  "right_up_empty"
        
        def addPiece(newSize,newStatusBoard):
            size[newSize][newStatusBoard] = ( size[newSize].get(newStatusBoard,0) + size[i][statusBoard] ) % (10**9 + 7)

        for i in range(len(size)-2):
            for statusBoard, item in size[i].items():    
                # add every title to the prev combinations of size i (every status of the board), generating a piece of size i+1 or i+2
                if statusBoard == "complete":  
                    addPiece(i + 1,"complete") # tiles = "vertical"
                    addPiece(i + 2,"right_down_empty") # tiles = "tromino_bottom_right_empty"
                    addPiece(i + 2,"right_up_empty") # tiles = "tromino_top_right_empty"
                    addPiece(i + 2,"complete") # tiles = "horizontal_up_down"
                elif statusBoard == "right_down_empty":
                    addPiece(i + 1, "complete") # tiles = "tromino_top_left_empty"
                    addPiece(i + 1, "right_up_empty") # tiles = "horizontal_down"
                elif statusBoard == "right_up_empty":
                    addPiece(i + 1, "complete") # tiles = "tromino_bottom_left_empty"
                    addPiece(i + 1, "right_down_empty") # tiles = "horizontal_up"

        if "complete" in size[-2]: return size[-2]["complete"]
        else: return -1




# same as the other, but the other is cleaner and a bit faster
# class Solution:
#     def numTilings(self, n: int) -> int:
#         # https://leetcode.com/problems/domino-and-tromino-tiling/?envType=study-plan-v2&envId=leetcode-75

#         tiles = ["vertical", "horizontal_up", "horizontal_down", "horizontal_up_down", "tromino_top_left_empty", "tromino_top_right_empty", "tromino_bottom_left_empty", "tromino_bottom_right_empty"]
#         size = [{} for _ in range(n+1)]
#         size[0] = {("complete"): 1} # "right_down_empty",  "right_up_empty"
#         for i in range(len(size)):
#             # print(1, size)
#             for statusBoard, item in size[i].items():    
#                 # add every title to the prev combinations of size x, generatin a piece of size x+1
#                 for statusTile in tiles:
#                     newSize = i
#                     newStatusBoard = None
#                     if statusBoard == "complete":  
#                         if statusTile == "vertical": newSize, newStatusBoard = newSize + 1, "complete"
#                         elif statusTile == "tromino_bottom_right_empty": newSize, newStatusBoard = newSize + 2, "right_down_empty"
#                         elif statusTile == "tromino_top_right_empty": newSize, newStatusBoard = newSize + 2, "right_up_empty"
#                         elif statusTile == "horizontal_up_down": newSize, newStatusBoard = newSize + 2, "complete"
#                     elif statusBoard == "right_down_empty":
#                         if statusTile == "tromino_top_left_empty": newSize, newStatusBoard = newSize + 1, "complete"
#                         elif statusTile == "horizontal_down": newSize, newStatusBoard = newSize + 1, "right_up_empty"
#                     elif statusBoard == "right_up_empty":
#                         if statusTile == "tromino_bottom_left_empty": newSize, newStatusBoard = newSize + 1, "complete"
#                         elif statusTile == "horizontal_up": newSize, newStatusBoard = newSize + 1, "right_down_empty"
#                     if newStatusBoard is not None and newSize < len(size):
#                         # print(i, statusBoard, statusTile, newSize, newStatusBoard)
#                         size[newSize][newStatusBoard] = ( size[newSize].get(newStatusBoard,0) + size[i][statusBoard] ) % (10**9 + 7)
#         # print(size)
#         if "complete" in size[-1]: return size[-1]["complete"]
#         else: return -1