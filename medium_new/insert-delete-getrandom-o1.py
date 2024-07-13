# Solution 1
# import random
# class RandomizedSet:
#     # https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1319913416/?envType=study-plan-v2&envId=top-interview-150
#     def __init__(self):
#         self.s = set()
#         self.arr = []
#         self.s_len = 0

#     def insert(self, val: int) -> bool:
#         if val not in self.s:
#             self.s.add(val)
#             self.arr.append(val)
#             self.s_len += 1
#             return True
#         return False

    
#     def remove(self, val: int) -> bool:
#         if val in self.s:
#             self.s.remove(val)
#             self.s_len -= 1

#             # Lets keep the arr.len() <= 2*s.len(). When it happens, we will simply replace the arr by the elements of s. We will spend O(n), but it will be done very few times. In average it would be O(1)
#             if self.s_len < len(self.arr)//2:
#                 self.arr = list(self.s)

#             return True
#         return False
        

# Solution 2 - Inspired in one of the submissions. Faster than the Solution 1
import random
class RandomizedSet:
    # https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/1319913416/?envType=study-plan-v2&envId=top-interview-150
    def __init__(self):
        self.s = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.s:
            # since we cannot pop an inner array element in O(1), we replace it with the last element of the array, and thet we pop the last arr element.
            val_idx, last_val = self.s[val], self.arr[-1]
            self.arr[val_idx] = last_val  # replace it with the last element from arr
            self.s[last_val] = val_idx
            self.arr.pop()
            del self.s[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)


#     def getRandom(self) -> int:
#         # Lets get an random element that in s. As long as the arr.len() is smaller than 2*s.len(), we need in the worse case, in average, run the loop 2 times in order to get an element that is in s.  Complexity of O(1)
#         element = random.choice(self.arr)
#         while not element in self.s: 
#             element = random.choice(self.arr)
        
#         return element


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()