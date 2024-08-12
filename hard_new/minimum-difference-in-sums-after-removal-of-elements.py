class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
        # the middle can range from n to 2n. The idea is removing the min elements form the left, and the max elements form the right. The problem is that the middle can change within a range ...
        # we will move the middle to the right from [n,2n]. We also have the min elments from the left part, and the max element from the right part. As we move the middle pointer ot the right, we add the new element to the left side heap, and remove the max from a harsh/heap that contains all the max form the left. The iadea is at each iteration, compute a new min in the left heap, and anew max in the right. That way we spend only o(logn) for each move of the pointer.  That way owr complexity will be O(nlogn)
        # O(nlogn)
        # nums = [n*-1 for n in nums]
        # obs: i inverted the logic. I did thinking that we must maximize the left, and minimize the right. But we have to do the oposite, sonce the problem ask to minimize the final diff. Because of that, i inverted the signs of the heaps. The maxheap would become min heap. But since im lazy to change names, i jast kept the way it was
        
        n = len(nums) // 3

        import heapq
        leftMinHeap = []
        rightMaxHeap = []
        rightMaxHeapAux = []
        removedFromRight = {}
        rightMaxHeapDict = {}

        totalLeft = 0
        totalLeftDrop = 0
        totalRight = 0
        totalRightDrop = 0

        # fill the heap (initial values). Initially we anly removed values from the right part, and none from the left
        # get total sum from right part
        for i in range(n,3*n):
            totalRight += nums[i]
            heapq.heappush(rightMaxHeapAux, nums[i])

        # get the sum of the min values from the right
        for i in range(n):
            maxValFromRight = heapq.heappop(rightMaxHeapAux)
            totalRightDrop += maxValFromRight # contains the sum of the min values from the right

            # create a heap and a harh with the nth min values from the right
            heapq.heappush(rightMaxHeap, -maxValFromRight)
            rightMaxHeapDict[maxValFromRight] = rightMaxHeapDict.get(maxValFromRight, 0) + 1

    
        # get total sum from left part. 
        for i in range(0, n):
            totalLeft += nums[i]
            # add nums[i] to the left min heap
            heapq.heappush(leftMinHeap, -nums[i])
            
            # # remove nums[i] from he right max heap. We will not remove it directly from the heap, because it is o(n). We will save it in a harsh, and latter on we skip these nums[i]
            # removedFromRight = removedFromRight.get(nums[i]) + 1

        # print(totalRight, totalRightDrop, rightMaxHeapDict, rightMaxHeap)
        # print(totalLeft, totalLeftDrop, leftMinHeap)
        
        sol = (totalLeft - totalLeftDrop) - (totalRight - totalRightDrop)

        # working in the middle range
        for i in range(n, 2*n):
            # print(i, totalRight, totalRightDrop, rightMaxHeapDict, rightMaxHeap)
            # print(i, totalLeft, totalLeftDrop, leftMinHeap)
            # the left side
            heapq.heappush(leftMinHeap, -nums[i])
            minValFromLeft = -heapq.heappop(leftMinHeap)
            totalLeftDrop += minValFromLeft
            totalLeft += nums[i]

            # the right side
            # remove nums[i] from he right max heap. We will not remove it directly from the heap, because it is o(n). We will save it in a harsh, and latter on we skip these nums[i]
            # removedFromRight = removedFromRight.get(nums[i]) + 1
            totalRight -= nums[i]

            if nums[i] in rightMaxHeapDict and rightMaxHeapDict[nums[i]] > 0: # if nums[i] is in the heap, then we can just remove it only
                rightMaxHeapDict[nums[i]] -= 1  
                # we should remove nums[i] from the heap, but it is expensive(O(n)). So lets just skip it when we find it in the nexr else statement (O(1)).
                totalRightDrop -= nums[i]

            else: # since nums[i] is not in the heap, we must remove it and also the max val from the heap
                maxValFromRight = -heapq.heappop(rightMaxHeap)
                while rightMaxHeapDict[maxValFromRight] == 0:  # we will skip the itens from the heap in which we have already "removed"
                    maxValFromRight = -heapq.heappop(rightMaxHeap)
                if rightMaxHeapDict[maxValFromRight] > 0: rightMaxHeapDict[maxValFromRight] -= 1
                totalRightDrop -= maxValFromRight

            diff = (totalLeft - totalLeftDrop) - (totalRight - totalRightDrop)
            # diff = -(totalLeft - totalLeftDrop) + (totalRight - totalRightDrop)
            sol = min(sol, diff)

        # print(i, totalRight, totalRightDrop, rightMaxHeapDict, rightMaxHeap)
        # print(i, totalLeft, totalLeftDrop, leftMinHeap)

        return sol

     
            
