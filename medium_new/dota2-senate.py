from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75

        r_queue = deque() # it will hold position of the party 'R' member
        d_queue = deque() # it will hold position of the party 'S' member

        for i, s in enumerate(senate):
            if s == 'R': r_queue.append(i)
            else: d_queue.append(i)

        while d_queue and r_queue:
            d = d_queue.popleft()
            r = r_queue.popleft()

            if d < r:
                d_queue.append(d+len(senate))
            else:
                r_queue.append(r+len(senate))

        return "Radiant" if not d_queue else "Dire"



# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         # https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75
        
#         time = 0
#         r_queue = deque() # it will hold position of the party 'R' member
#         d_queue = deque() # it will hold position of the party 'S' member

#         for i, s in enumerate(senate):
#             if s == 'R': r_queue.append(i)
#             else: d_queue.append(i)

#         i, j = 0, 0
#         for time in range(0, len(senate)):
#             if (not d_queue) or j>=len(d_queue): return "Radiant"
#             if (not r_queue) or i>=len(r_queue): return "Dire"
#             if r_queue[i] == time: 
#                 d_queue.popleft()
#                 j = j-1
#             elif d_queue[j] == time: 
#                 r_queue.popleft()
#                 i = i-1
#             else:
#                 i, j = i+1, j+1

