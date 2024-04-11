# https://leetcode.com/problems/task-scheduler/submissions/

# I SOLVED IT BUT 1011ms Beats 5.02%of users with Python3. So there is a better solution out there

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # lets try a greedy approach. Start from the most repeated word, and try to use this word as soon as possible again, as soon the unit of time was met. Create a priority sequence, maybe a priority queue (max/min heap). Exp: if we have added A first, the priority is using another A. But since using another A in sequence would cost and IDLE, then lets check if we can use the second letter in the priority task. If we can, then we use that task.  

        def Solution1():
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

        def Solution2():
            # i am redoing this question 4 months later, but the runtime is still slow ...
            # a b i a b i i b
            # b a i b a i b
            # considerations
            # 1 - priority is to use the numbers that repeat the most
            # 2 - set a clock, a time in which each word is available to use. As soon it is avalilable, we will use it. Remember that the priority is the ones tha trepeat the most
            # use priority heap o(i) to pop() o(logn) to add an item -> O(nlogn)

            count_tasks = {}
            for task in tasks:
                count_tasks[task] = count_tasks.get(task,0) + 1
            
            heap = []
            for task, count in count_tasks.items():
                heap.append( [0, -count, task] ) # clock = 0, -1*count because we are using a min heap

            import heapq # min heap
            heapq.heapify(heap)

            global_clock = 0
            while heap:
                clock, count, task = heapq.heappop(heap) # get the min element (clock, count)
                
                # update the global clock
                if clock < global_clock:
                    clock = global_clock
                global_clock = clock + 1
                
                # update the task
                clock = clock + n + 1 # we can do the task after n cycles
                count = count + 1 # we add 1 because we did -1*count
                
                # put it back to the heap
                if count < 0:
                    heapq.heappush(heap, [clock, count, task] )
                
                # we need to update the value of the clock for every task in the queue
                for i in range(len(heap)):
                    heap[i][0] = max(heap[i][0], global_clock)
                heapq.heapify(heap)

                print(global_clock, clock, count, task, heap)

            return global_clock # just add 1 because for the answer the have to count from 1 instead of from 0 

        # def Solution3(): # a solution from Submissions
        #     from collections import defaultdict
        #     counts = defaultdict(int)
        #     heap = []
        #     for t in tasks: counts[t] += 1
        #     for t in counts.keys(): heap.append((0,t))
        #     heapq.heapify(heap)
        #     turn = 0
        #     while heap:
        #         if turn < heap[0][0]:
        #             turn += 1
        #             continue
        #         v,k = heapq.heappop(heap)
        #         counts[k] -= 1
        #         if counts[k] > 0: heapq.heappush(heap,(v + n + 1,k))
        #         print(turn,v,k, heap)
        #         turn += 1
                
        #     return turn

        return Solution2()
