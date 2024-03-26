# class RecentCounter:
#     # https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75
#     def __init__(self):
#         self.counter = []
        

#     def ping(self, t: int) -> int:
#         self.counter.append(t)
#         numRequests = 0
#         start = t - 3000
#         for c in reversed(self.counter):
#             if c >= start:
#                 numRequests += 1
#             else:
#                 break
        
#         # for i in range(len(self.counter)-1,-1,-1):
#         #     if self.counter[i] >= start:
#         #         numRequests += 1
#         #     else:
#         #         break
#         return numRequests

         
        


# # Your RecentCounter object will be instantiated and called as such:
# # obj = RecentCounter()
# # param_1 = obj.ping(t)




class RecentCounter:
    # https://leetcode.com/problems/number-of-recent-calls/?envType=study-plan-v2&envId=leetcode-75
    def __init__(self):
        self.counter = deque()
        
    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[0] < t - 3000:
            self.counter.popleft()
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)