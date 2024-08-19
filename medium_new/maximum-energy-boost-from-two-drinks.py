class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/
        # based on a submission's solution. Use dp, keeping track of the best solution from top, and bottom
        # time complexity: O(n) space O(1)
        pathA, pathB = 0, 0
        for i in range(len(energyDrinkA)):
            pathA, pathB = max(pathA + energyDrinkA[i], pathB), max(pathB + energyDrinkB[i], pathA)
        return max(pathA, pathB)



# # it did not work
# class Solution:
#     def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
#         # is it better to keep in the same drink, or change drinks even losing 1 hour (skipping one pos)

#         myDrink = [0,0,0,0,0,0,0] + energyDrinkA + [0,0,0,0,0,0,0,0,0]
#         otherDrink =  [0,0,0,0,0,0,0] + energyDrinkB + [0,0,0,0,0,0,0,0,0]
#         output = 0
#         for i in range(len(myDrink)-8):
#             # Check if we showld skip i and switch
#             if otherDrink[i+1] > myDrink[i] + myDrink[i+1] + myDrink[i+2] or otherDrink[i+1] + otherDrink[i+2] > myDrink[i] + myDrink[i+1] + myDrink[i+2] + myDrink[i+3]  or otherDrink[i+1] + otherDrink[i+2] + otherDrink[i+3]> myDrink[i] + myDrink[i+1] + myDrink[i+2] + myDrink[i+3] + myDrink[i+4] or otherDrink[i+1] + otherDrink[i+2] + otherDrink[i+3] + otherDrink[i+4]> myDrink[i] + myDrink[i+1] + myDrink[i+2] + myDrink[i+3] + myDrink[i+4] + myDrink[i+5] or otherDrink[i+1] + otherDrink[i+2] + otherDrink[i+3] + otherDrink[i+4]  + otherDrink[i+5] > myDrink[i] + myDrink[i+1] + myDrink[i+2] + myDrink[i+3] + myDrink[i+4] + myDrink[i+5] + myDrink[i+6] or otherDrink[i+1] + otherDrink[i+2] + otherDrink[i+3] + otherDrink[i+4]  + otherDrink[i+5] + otherDrink[i+6]> myDrink[i] + myDrink[i+1] + myDrink[i+2] + myDrink[i+3] + myDrink[i+4] + myDrink[i+5] + myDrink[i+6] + myDrink[i+7] or otherDrink[i+1] + otherDrink[i+2] + otherDrink[i+3] + otherDrink[i+4]  + otherDrink[i+5] + otherDrink[i+6]  + otherDrink[i+7]> myDrink[i] + myDrink[i+1] + myDrink[i+2] + myDrink[i+3] + myDrink[i+4] + myDrink[i+5] + myDrink[i+6] + myDrink[i+7] + myDrink[i+8]:
#                 # we can swich and switch back to the i+3 if we want in the next iterations
#                 myDrink, otherDrink = otherDrink, myDrink
#             else:
#                 output += myDrink[i]


#         return output


