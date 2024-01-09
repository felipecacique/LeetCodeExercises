# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # my previous solution worked  and was the best solution. The solution in https://www.youtube.com/watch?v=QHXET1G9Y5U&ab_channel=NeetCode is the same as mine, but his implementation was a little bit more compart/eficient. So I brought some of it to my implementation, and it got faster. Time O(n).
        # Runtime 103ms Beats 78.91%of users with Python3   Memory 17.06MB Beats 78.73%of users with Python3
        
        # t_count = Counter(t)

        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c,0) + 1
        
        start, end = 0, 0
        size_solution, best_solution_id = float('inf'), (0,0)
        subs_count, complete, n = {} , 0, len(s)
        distinct_char = len(t_count.keys())

        # for char in t_count.keys():
        #     subs_count[char] = 0

        for end in range(0,len(s)):

            c = s[end]

            # if c in t_count: # skip char that is not in t

            # subs_count[c] += 1
            subs_count[c] = 1 + subs_count.get(c,0)
            
            if c in t_count and subs_count[c] == t_count[c]: # i have just added 1, and now it is equal, so one more complete
                complete += 1

            while complete >= distinct_char: # if it is complete

                d = s[start]

                # if d in t_count: # skip char that is not in t

                # we have a possible solution
                # new_size_solution =  end - start + 1
                if end - start + 1 < size_solution:
                    best_solution_id = (start, end+1)
                    size_solution = end - start + 1
                        
                subs_count[d] -= 1
                if d in t_count and subs_count[d] == t_count[d]-1: # i have just removed 1, and now it is less
                    complete -= 1

                start += 1
        
            # end += 1

        return s[best_solution_id[0] : best_solution_id[1]]
    
    
    
    
    
# # my best solution, it the best solution  
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # 2 pointes, stars and end starting from i=0. The move them until we fin the first "solution", having the start_s and end_s. Then we drop the fisrt element of this subarray in the position start_s, and update the start_s to be the next letter that is exists in t (we will use a queue for that). Then move end_s to the right until we get another "solution", and repeate this process storing always the best solution. The called "solution" is a substring that meets the criteria, that is every character in t (including duplicates) must be included in the window. How to do it? we will use a letter count dictionary, we will build it as we move our pointers .... Then we use it to check if the substring is a solution (can we do better?) ... But the complexity might be O(26), since we have to compare the count for each alphabet letter. So the total complexity of the algorithm will be O(26*n)
        
#         # criar queue com or par (letra, tamanho), onde a letra é a letra em s que existe em t, e o tamanho é o numero de caracteres na frente dela, que nao percence a t, incluindo ela. Ou seja, são os caracteres entre ela e a proxima letra que pertence a t. Assim conseguimos recomputar o tamanho da substring
#     # faremos uma abordagem similar á tentativa acima, mas agora pegrando direteamente da queue, sem ter que trabalhar mais com a string s, sem ter que iterala. A minha abotagem acima funcionou para muitos casos, mas em alguns ele fahlou. 
#     # devemos popleft ate que nao seja mais possivel (isso diminui o tamanho da substring) e so depois movimentamos o penteiro 'end' ate que complete() == true. Mas devera haver uma aborgem um pouco diferente pra o end, usando apenas a queue, e nao mais s. 
#     # time O(26*n) but as we are using the auxiliar complete var, we have reduced to  O(n)
            

#         # creating the dictionary with the letter counts in t
#         t_count = {}
#         for char in t:
#             if not char in t_count:
#                 t_count[char] = 1
#             else:
#                 t_count[char] += 1
        
#         start = 0
#         end = 0
#         best_solution = ""
#         size_solution = float('inf')
#         best_solution_id = (0,0)
#         subs_count = {} 
#         complete = 0 # count the number of letter that are complete
#         distinct_char = len(t_count.keys())
#         n = len(s)


#         for char in t_count.keys():
#             subs_count[char] = 0

#         while end < n:

#             if s[end] in t_count: # skip char that is not in t

#                 subs_count[s[end]] += 1
#                 if subs_count[s[end]] == t_count[s[end]]: # i have just added 1, and now it is equal, so one more complete
#                     complete += 1
                
#                 # flag = False
#                 # last_start = start

#                 while start < n:

#                     if s[start] in t_count: # skip char that is not in t

#                         if complete < distinct_char: # if is not complete
#                             break
#                         else: 
#                             # flag = True
#                             # last_start = start
#                             # compute the size of the solution
#                             new_size_solution =  end - start + 1
#                             if new_size_solution < size_solution:
#                                 best_solution_id = (start, end+1)
#                                 size_solution = new_size_solution
                                
#                         subs_count[s[start]] -= 1
#                         if subs_count[s[start]] == t_count[s[start]]-1: # i have just removed 1, and now it is less
#                             complete -= 1

#                     start += 1
            
#                 # if flag == True:
#                 #     # compute the size of the solution
#                 #     new_size_solution =  end - last_start + 1
#                 #     if new_size_solution < size_solution:
#                 #         best_solution_id = (last_start, end+1)
#                 #         size_solution = new_size_solution
#                 #     flag = False
#             end += 1
        
#         # return best_solution
#         return s[best_solution_id[0] : best_solution_id[1]]








# solution using an auxiliar queue
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # 2 pointes, stars and end starting from i=0. The move them until we fin the first "solution", having the start_s and end_s. Then we drop the fisrt element of this subarray in the position start_s, and update the start_s to be the next letter that is exists in t (we will use a queue for that). Then move end_s to the right until we get another "solution", and repeate this process storing always the best solution. The called "solution" is a substring that meets the criteria, that is every character in t (including duplicates) must be included in the window. How to do it? we will use a letter count dictionary, we will build it as we move our pointers .... Then we use it to check if the substring is a solution (can we do better?) ... But the complexity might be O(26), since we have to compare the count for each alphabet letter. So the total complexity of the algorithm will be O(26*n)
        
#         # criar queue com or par (letra, tamanho), onde a letra é a letra em s que existe em t, e o tamanho é o numero de caracteres na frente dela, que nao percence a t, incluindo ela. Ou seja, são os caracteres entre ela e a proxima letra que pertence a t. Assim conseguimos recomputar o tamanho da substring
#     # faremos uma abordagem similar á tentativa acima, mas agora pegrando direteamente da queue, sem ter que trabalhar mais com a string s, sem ter que iterala. A minha abotagem acima funcionou para muitos casos, mas em alguns ele fahlou. 
#     # devemos popleft ate que nao seja mais possivel (isso diminui o tamanho da substring) e so depois movimentamos o penteiro 'end' ate que complete() == true. Mas devera haver uma aborgem um pouco diferente pra o end, usando apenas a queue, e nao mais s. 
#     # time O(26*n) but as we are using the auxiliar complete var, we have reduced to  O(n)
            

#         # creating the dictionary with the letter counts in t
#         t_count = {}
#         for char in t:
#             if not char in t_count:
#                 t_count[char] = 1
#             else:
#                 t_count[char] += 1
        
#         queue = [] # holds the char* thas exist in t as it apears in s, and also its id in s

#         dist = 1
#         for i, c in enumerate(s):
#             if c in t_count:
#                 queue.append( [c, i] )
    
#         start = 0
#         end = 0
#         best_solution = ""
#         size_solution = float('inf')
#         best_solution_id = (0,0)
#         subs_count = {} 
#         complete = 0 # count the number of letter that are complete
#         distinct_char = len(t_count.keys())
#         n = len(queue)

#         for char in t_count.keys():
#             subs_count[char] = 0

#         while end < n:

#             subs_count[queue[end][0]] += 1
#             if subs_count[queue[end][0]] == t_count[queue[end][0]]: # i have just added 1, and now it is equal, so one more complete
#                 complete += 1
            
#             flag = False
            
#             while start < n:

#                 if complete < distinct_char: # if is not complete
#                     break
#                 else: 
#                     flag = True
#                     # # compute the size of the solution
#                     # new_size_solution =  queue[end][1] - queue[start][1] + 1
#                     # if new_size_solution < size_solution:
#                     #     # best_solution = s[queue[start][1] : queue[end][1]+1]
#                     #     best_solution_id = (queue[start][1], queue[end][1]+1)
#                     #     # print('s s ', best_solution, best_solution_id)
#                     #     size_solution = new_size_solution
                        
#                 subs_count[queue[start][0]] -= 1
#                 if subs_count[queue[start][0]] == t_count[queue[start][0]]-1: # i have just removed 1, and now it is less
#                     complete -= 1

#                 start += 1
            
#             if flag == True:
#                 # compute the size of the solution
#                 new_size_solution =  queue[end][1] - queue[start-1][1] + 1
#                 if new_size_solution < size_solution:
#                     # best_solution = s[queue[start][1] : queue[end][1]+1]
#                     best_solution_id = (queue[start-1][1], queue[end][1]+1)
#                     # print('s s ', best_solution, best_solution_id)
#                     size_solution = new_size_solution

#             end += 1
        
#         # return best_solution
#         return s[best_solution_id[0] : best_solution_id[1]]







# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         # 2 pointes, stars and end starting from i=0. The move them until we fin the first "solution", having the start_s and end_s. Then we drop the fisrt element of this subarray in the position start_s, and update the start_s to be the next letter that is exists in t (we will use a queue for that). Then move end_s to the right until we get another "solution", and repeate this process storing always the best solution. The called "solution" is a substring that meets the criteria, that is every character in t (including duplicates) must be included in the window. How to do it? we will use a letter count dictionary, we will build it as we move our pointers .... Then we use it to check if the substring is a solution (can we do better?) ... But the complexity might be O(26), since we have to compare the count for each alphabet letter. So the total complexity of the algorithm will be O(26*n)
        
#         # criar queue com or par (letra, tamanho), onde a letra é a letra em s que existe em t, e o tamanho é o numero de caracteres na frente dela, que nao percence a t, incluindo ela. Ou seja, são os caracteres entre ela e a proxima letra que pertence a t. Assim conseguimos recomputar o tamanho da substring
#     # faremos uma abordagem similar á tentativa acima, mas agora pegrando direteamente da queue, sem ter que trabalhar mais com a string s, sem ter que iterala. A minha abotagem acima funcionou para muitos casos, mas em alguns ele fahlou. 
#     # devemos popleft ate que nao seja mais possivel (isso diminui o tamanho da substring) e so depois movimentamos o penteiro 'end' ate que complete() == true. Mas devera haver uma aborgem um pouco diferente pra o end, usando apenas a queue, e nao mais s. 
            


#         # creating the dictionary with the letter counts in t
#         t_count = {}
#         for char in t:
#             if not char in t_count:
#                 t_count[char] = 1
#             else:
#                 t_count[char] += 1

#         # # creating the dictionary with the letter counts in s
#         # s_count = {} 
#         # for char in s:
#         #     if not char in s_count:
#         #         s_count[char] = 1
#         #     else:
#         #         s_count[char] += 1
  
#         # # lets check is a solution exists
#         # for char in t_count:
#         #     if not char in s_count:
#         #         return ""
#         #     else:
#         #         if s_count[char] < t_count[char]: # the count in s must be equal or greatter than the count in t, otherwise no solution
#         #             return ""


#         # the solution exist, so we can proceed with our method

#         def complete(subs_count):

#             # check is all char of t is in the substring 
#             for char in t_count:
#                 if not char in subs_count:
#                     return False
#                 else:
#                     if subs_count[char] < t_count[char]: # the count in s must be equal or greatter than the count in t, otherwise no solution
#                         return False
#             return True

#         queue = [] # holds the char* thas exist in t as it apears in s, and also the distance between these char (number of char that is not in t that comes after char* in s)

#         dist = 1
#         for i, c in enumerate(s):
#             if c in t_count:
#                 dist = 1
#                 queue.append( [c, dist, i] )
#             else:
#                 if not len(queue) == 0:
#                     queue[-1][1] += 1
        
#         # print(queue)

#         start = 0
#         end = 0
#         best_solution = ""
#         size_solution = float('inf')
#         subs_count = {} 

#         while end < len(queue):


#             if not queue[end][0] in subs_count:
#                 subs_count[queue[end][0]] = 1
#             else:
#                 subs_count[queue[end][0]] += 1
            

#             while start < len(queue):
#                 # print(queue[start:end+1], start, end, subs_count)
#                 if not complete(subs_count):
#                     break
#                 else: 
#                     # compute the best solution
#                     new_solution = queue[start:end+1]
                    
#                     # compute the size
#                     new_size_solution =  new_solution[-1][2] - new_solution[0][2] + 1
#                     # for c, dist, i in new_solution[:-1]:
#                     #     new_size_solution += dist
#                     # new_size_solution += 1

#                     # print("kkk ", new_solution, new_size_solution, s[new_solution[0][2] : new_solution[-1][2]+1])

#                     if new_size_solution < size_solution:
#                         best_solution = s[new_solution[0][2] : new_solution[-1][2]+1]
#                         # best_solution = new_solution
#                         size_solution = new_size_solution
                        

#                 subs_count[queue[start][0]] -= 1

#                 start += 1

#             end += 1
#         # print(best_solution)
#         # return s[best_solution[0][2] : best_solution[-1][2]+1]
#         return best_solution