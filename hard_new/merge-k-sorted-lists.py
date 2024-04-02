# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # https://leetcode.com/problems/merge-k-sorted-lists/?envType=study-plan-v2&envId=top-interview-150
        
        def Solution1(lists): # works but long and not optimal O(k*m)
            clean_list = []
            for l in lists:
                if l:
                    clean_list.append(l)
            lists = clean_list

            if not lists:
                return None

            def linkedListToArray(head):
                arr = []
                def dfs(node):
                    if not node: return
                    arr.append(node.val)
                    dfs(node.next)
                dfs(head)
                return arr
            
            arrs = []

            for linkedList in lists:
                arrs.append(linkedListToArray(linkedList))
            
            
            mergedArr = []
            totalLen = 0
            for arr in arrs:
                totalLen += len(arr)
            
            arrs = [ [arr, 0] for arr in arrs]
        
            while len(mergedArr) < totalLen:
                smaller = float('inf')
                smallerArrith = 0
                k = 0
                for arr, i in arrs:
                    if i < len(arr):
                        if arr[i] < smaller:
                            smaller = arr[i]
                            smallerArrith = k
                    k += 1
                arrs[smallerArrith][1] += 1
                mergedArr.append(smaller)

                 

            head = ListNode(mergedArr[0])
            node = head
            for val in mergedArr[1:]:
                node.next = ListNode(val)
                node = node.next
            
            return head


        def Solution2(lists): # solution based in one of the best solution that i saw from other people. Using heap. O(nlogn)
            
            import heapq
            
            if not lists: 
                return None

            heap = []

            # insert the nodes to the heap
            for idx, l in enumerate(lists):
                if l: 
                    heapq.heappush(heap, (l.val, idx, l))
            
            # try to append to curr heap
            node = ListNode(-1)
            head = node
            while heap:
                val, idx, n = heapq.heappop(heap) # pop the smallest
                node.next = ListNode(val)
                node = node.next
                if n.next:
                    heapq.heappush(heap,(n.next.val, idx, n.next))
            
            return head.next

        return Solution2(lists)
