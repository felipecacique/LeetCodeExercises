class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # O(n^2)
        arr = nums
        while len(arr) > 1:
            newArr = []
            for i in range(len(arr)-1):
                newArr.append((arr[i]+arr[i+1]))
            arr = newArr
        
        return arr[0]%10
            

