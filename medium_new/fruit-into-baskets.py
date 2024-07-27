class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #https://leetcode.com/problems/fruit-into-baskets/
        # find the longest subsequence that has only 2 distinc elements
        
        repeated = [-1,0] # (fruit, count) stores the fruit repeated in sequence and its ammount
        output = 0
        fruit1, fruit2 = -1, -2
        fruitCount = {-1:0, -2:0}
        for i in range(0,len(fruits)):
                
            fruitCount[fruits[i]] = fruitCount.get(fruits[i], 0) + 1
            if not fruits[i] in [fruit1, fruit2]:
                fruit1 = repeated[0]
                fruit2 = fruits[i]
                fruitCount[fruit1] = repeated[1]
                fruitCount[fruit2] = 1

            if fruits[i] == repeated[0]: repeated[1] += 1
            else: repeated = [fruits[i],1]
                
            output = max(output, fruitCount[fruit1] + fruitCount[fruit2])
            
        return output 
            