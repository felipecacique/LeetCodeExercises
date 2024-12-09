class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # O(n)
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        return len([num for num, count in counts.items() if num > 0])