class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
        # sliding window approach adding flower by flower

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
                flowerbed[0] = 1

        if flowerbed[0] == 0 and flowerbed[0+1] == 0:
                n -= 1
                flowerbed[0] = 1
            
        if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-1-1] == 0:
                n -= 1
                flowerbed[len(flowerbed)-1] = 1

        for i in range(0, len(flowerbed)):

            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1

            if n <= 0:
                return True
        
        return False

