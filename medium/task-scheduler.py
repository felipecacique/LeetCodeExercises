# https://leetcode.com/problems/task-scheduler/submissions/

# I SOLVED IT BUT 1011ms Beats 5.02%of users with Python3. So there is a better solution out there

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # lets try a greedy approach. Start from the most repeated word, and try to use this word as soon as possible again, as soon the unit of time was met. Create a priority sequence, maybe a priority queue (max/min heap). Exp: if we have added A first, the priority is using another A. But since using another A in sequence would cost and IDLE, then lets check if we can use the second letter in the priority task. If we can, then we use that task.  


        task_dict = {} # holds the task and the number of time it repeats

        for task in tasks:
            if not task in task_dict:
                task_dict[task] = 1
            else:
                task_dict[task] += 1
    
        task_count = [] # holds the pairs "number of time it repeats" and the "taks" in tuples, and in this order. So we can 'sort' by the repeated count in out priority queue (max/min heap).

        for task, count in task_dict.items():
            task_count.append( [-count, task] ) # the priority is higher count (remaing number of tasks). Sor we multiply count by -1, so that we can sort it and get tme min, in a priority queue. 

        idle_count = 0
        processed_tasks = 0

        import heapq

        heap = task_count
        heapq.heapify(heap)

        from collections import deque
        queue = deque()

        while True:
            while len(queue) < n + 1 and  len(heap) > 0:
                remaing, task = heapq.heappop(heap) # get the min
                queue.append( [ remaing, task ] ) # by adding at the end, there will be n-1 tasks ahead to be popped in the queue. Which means that when the this task is taken, the countdown has already reach 0, and no idle would be needed. 
             
            while len(queue) < n + 1:
                queue.append( [float('inf'), 'idle'] ) # fll the empty spaces with idle
            

            remaining, task = queue.popleft() # get the most priority task
            
            new_remaining = remaining + 1 # subtract one task. We sum instead of subtracting becase we have multiplied remaing by -1
            if new_remaining < 0:
                # put it back to the heap
                heapq.heappush(heap, [new_remaining, task])
            
            if task != 'idle':
                processed_tasks += 1
            
            if processed_tasks == len(tasks):    # we have already processed all tasks, so end the loop
                break
         
            # count the number of idles
            if task == 'idle':
                idle_count += 1

        return idle_count + processed_tasks


