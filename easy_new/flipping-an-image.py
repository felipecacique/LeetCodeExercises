class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # https://leetcode.com/problems/flipping-an-image/
        for i in range(len(image)):
            image[i] = list(reversed(image[i]))
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
                    
        return image