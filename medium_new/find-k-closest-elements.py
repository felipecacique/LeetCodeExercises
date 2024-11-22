class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # https://leetcode.com/problems/find-k-closest-elements/
        # binary search and pointers
        # O(logn + k + k.log(k))

        arr = [float('-inf')] + arr + [float('inf')]
        l, r = 0, 0
        output = []

        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] > x:
                right = mid 
            else:
                left = mid + 1

        l = left - 1
        r = left   
 
        while len(output) < k:
            if abs(arr[l] - x) <= abs(arr[r] - x):
                output.append(arr[l])
                l -= 1
            else:
                output.append(arr[r])
                r += 1
        
        return sorted(output) #  k.log(k)
