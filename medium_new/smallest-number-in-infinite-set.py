import heapq # min heap
class SmallestInfiniteSet:
    # https://leetcode.com/problems/smallest-number-in-infinite-set/?envType=study-plan-v2&envId=leetcode-75
    def __init__(self):
        self.addedNums = []
        self.n = 1
        heapq.heapify(self.addedNums)
        self.addedNumsSet = set() # to not add repeated nums into the heap
        

    def popSmallest(self) -> int:
        if self.addedNums:
            smallestInHeap = heapq.nsmallest(1, self.addedNums)[0]
            if smallestInHeap < self.n:
                heapq.heappop(self.addedNums)
                self.addedNumsSet.remove(smallestInHeap)
                return smallestInHeap
            elif smallestInHeap == self.n:
                heapq.heappop(self.addedNums)
                self.addedNumsSet.remove(smallestInHeap)
        smallest = self.n 
        self.n += 1
        return smallest

    
    def addBack(self, num: int) -> None:
        if num not in self.addedNumsSet:
            if num < self.n:
                heapq.heappush(self.addedNums, num)
                self.addedNumsSet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)