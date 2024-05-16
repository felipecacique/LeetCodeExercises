class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # https://leetcode.com/problems/boats-to-save-people/?envType=daily-question&envId=2024-05-04
        # select pairs in which sum is maximixed. Get the fattest person with the slimmest person in the same boat
        # O(nlogn) because sort

        people = sorted(people)

        left = 0
        right = len(people) - 1
        num_boats = 0

        while left <= right:

            if right == left: 
                # one person left
                num_boats += 1
                break 

            elif people[right] + people[left] <= limit:
                # the 2 fit in the same boat
                num_boats += 1
                right -= 1
                left += 1
            
            else:
                # only the fat fit in the boat, so he will go alone
                num_boats += 1
                right -= 1

        return num_boats


