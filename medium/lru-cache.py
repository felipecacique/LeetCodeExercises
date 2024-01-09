# https://leetcode.com/problems/lru-cache/description/

class LRUCache:
    #  if exceeds the capacity, we have to evict the least recently used key. Thta is the trickest part. To handle this we will create a queue, and we add the keys one by one as it apears on put. When we gtt the key, we would desire to remove it from the queue and add it to the end, however it is time consuming. We will just add a repeated key at the end of the queue, and have an auxiliary disctionary (repeated_dict) to hold the count for that key in the queue. When capacity is full, the len(queue_unique_keys) >= capacity, which actually in our implementation it will be len(queue_repeated_keys) >= capacity + count_repeated_keys, then we must pop the the fist element in the queue. And if the next element is duplicated (we check in the repeated_dict to know that), we pop it, and so on, untill we fing a key that is not duplicated. In other words, in our implementation, intead of removing the duplicated keys when it appears, we will remove it  later, during our pop operation. 

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.repeated_dict = {}
        self.queue = deque()
        self.repeated_count = 0
        

    def get(self, key: int) -> int:
        
        if key in self.d:
            self.queue.append(key)
            self.repeated_dict[key] += 1
            self.repeated_count += 1
            return self.d[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        # we add the key
        if key in self.d:
            self.d[key] = value
            self.queue.append(key)
            self.repeated_dict[key] += 1
            self.repeated_count += 1
        else:
            self.d[key] = value
            self.queue.append(key)
            self.repeated_dict[key] = 0


        # if exceeds the capacity, we have to evict the least recently used key (and duplicates)
        while len(self.queue) > self.capacity + self.repeated_count:
            
            key_evict = self.queue.popleft()
            
            if self.repeated_dict[key_evict] > 0: # removing diplicates (key in self.repeated_dict and) 
                self.repeated_dict[key_evict] -= 1
                self.repeated_count -= 1
            
            else : # evicting the least recently used key
                del self.d[key_evict]
                del self.repeated_dict[key_evict]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)