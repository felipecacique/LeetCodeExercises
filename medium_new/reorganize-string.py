class Solution:
    def reorganizeString(self, s: str) -> str:
        # https://leetcode.com/problems/reorganize-string/?envType=problem-list-v2&envId=7p5x763&sorting=W3sic29ydE9yZGVyIjoiREVTQ0VORElORyIsIm9yZGVyQnkiOiJGUkVRVUVOQ1kifV0%3D&page=1
        # time O(nlogn) because heaps   space O(n)
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        
        import heapq
        heap = [(-count, c) for c, count in counts.items()]
        heapq.heapify(heap)

        ans = [""]
        while heap:
            if heap[0][1] != ans[-1]:
                count, c = heapq.heappop(heap)
                ans.append(c)
                if count+1 < 0: heapq.heappush(heap, (count+1,c))

            elif heap[0][1] == ans[-1]:
                count_, c_ = heapq.heappop(heap)
                
                if not heap: return ""
                count, c = heapq.heappop(heap)
                ans.append(c)
                if count+1 < 0: heapq.heappush(heap, (count+1,c))

                heapq.heappush(heap, (count_,c_))

        return "".join(ans)