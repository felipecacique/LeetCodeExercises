class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        # https://leetcode.com/problems/high-access-employees/
        # o(nlogn) using sort and monotonic stack representing the 60 min window

        from collections import defaultdict
        from collections import deque

        output = set()
        nameAccess = defaultdict(list)

        # Create a dictionary with {name:["1230", "2150" ... ], name2: [ ... ] }
        for access_time in access_times:
            name = access_time[0]
            # transformando horario em minutos decorrentes do dia
            hourAccess = int(access_time[1][0])*10 + int(access_time[1][1]) 
            minAccess = int(access_time[1][2])*10 + int(access_time[1][3]) 
            minutesTotal = hourAccess*60+minAccess
            nameAccess[name].append(minutesTotal)
        
        # Use queue representing a window of 60 min, that has (start, end). The end is the accessTime, and the start -s end - 60 min. If we find numbers smaller than start in the queue, then we must pop them
        for name in nameAccess:
            nameAccess[name].sort()
            queue = deque()
            for accessTime in nameAccess[name]:
                start = accessTime - 60
                queue.append(accessTime)
                while queue and queue[0] <= start: # keep a monitonic queue conatining only the times for the 60 min window, ending on accessTime
                    queue.popleft()
                if len(queue) >= 3:
                    output.add(name)
                    break
        
        return list(output)


# class Solution:
#     def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
#         # https://leetcode.com/problems/high-access-employees/
#         # o(120*n) = o(n)

#         from collections import defaultdict
#         output = set()
#         d = defaultdict(int)

#         for access_time in access_times:
#             name = access_time[0]
#             # transformando horario em minutos decorrentes do dia
#             timeAccess = list(access_time[1])
#             hourAccess = int(timeAccess[0])*10 + int(timeAccess[1]) 
#             minAccess = int(timeAccess[2])*10 + int(timeAccess[3]) 
#             minutesTotal = hourAccess*60+minAccess
#             # Adicionar item em d
#             d[(name, minutesTotal)] += 1
        
#         names = set([item[0] for item, value in d.items()]) # get all the names

#         nameCount = defaultdict(int)    
#         for name in names:
#             for i in range(-60,1440):
#                 start = i - 30
#                 end = i + 29
#                 nameCount[name] += d[(name, end)]
#                 nameCount[name] -= d[(name, start-1)]
#                 if nameCount[name] >= 3:
#                     output.add(name)
#                     break

#         return list(output)
            

# class Solution:
#     def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
#         # https://leetcode.com/problems/high-access-employees/
#         # o(120*n) = o(n) ops, actually is o(nlog) because we have to sort it in order to work
#         output = set()
#         access_times = sorted(access_times)
#         from collections import defaultdict
#         d = defaultdict(int)
#         # {("a","1045"):5}
#         for access_time in access_times:

#             # Adicionar item em d
#             d[tuple(access_time)] += 1
#             # print(d)
            

#             name = access_time[0]

#             if name in output:
#                 continue



#             # transformando horario em minutos decorrentes do dia
#             timeAccess = list(access_time[1]) # ['0', '5', '4', '9']
#             hourAccess = int(timeAccess[0])*10 + int(timeAccess[1]) # 5 h
#             minAccess = int(timeAccess[2])*10 + int(timeAccess[3]) # 49 min
#             minutesTotal = hourAccess*60+minAccess # 349
#             # print(minutesTotal)
#             #start = max(minutesTotal - 60, -1) # 289
#             #end = min(minutesTotal + 60, 24*60) # 409
#             start = minutesTotal - 60 # 289
#             end = minutesTotal + 60 # 409
            
#             def getCount(start, end):
#                 # Verificar se o intervalo existe dentro de d
#                 count = 0
#                 for time in range(start, end):
#                     # transformacao inversa do horario
#                     hour = time//60 # 6hs
#                     minute = time%60 # 49 min
#                     hourStr = str(hour) if hour >= 10 else '0' + str(hour)
#                     minStr = str(minute) if minute >= 10 else '0' + str(minute)
#                     timeAccessLookUp = hourStr + minStr # '0649'

#                     access_time_lookup = (name, timeAccessLookUp) # ('a', '0648')
#                     if access_time_lookup in d:
#                         count += d[access_time_lookup] # adiciono a contagem
                    
#                     if count >= 3: # this guy is high-access
#                         output.add(access_time[0])
#                         break

#             getCount(start+1, minutesTotal+1)
#             # getCount(minutesTotal, end)

#         return list(output)
