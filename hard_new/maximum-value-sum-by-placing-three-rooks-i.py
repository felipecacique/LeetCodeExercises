class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        # https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/description/
        # do a bfs qith a priority heap. We sort all the numbers and start with the mest pair, that has the higher sum. Then we use a heap and do the searching, searching for the neighbouring candidatesm prioritizing the ones with higher totalSum first
        m, n = len(board), len(board[0])

        valuePos = []
        for j in range(m):
            for i in range(n):
                valuePos.append((board[j][i], j, i))
        

        valuePos = sorted(valuePos, reverse = True)


        import heapq
        rooks1, rooks2, rooks3 = valuePos[0], valuePos[0], valuePos[0]
        totalSum = board[rooks1[1]][rooks1[2]] + board[rooks2[1]][rooks2[2]] + board[rooks3[1]][rooks3[2]]
        heap = [(-totalSum, 0, 0, 0)] # stores the index of the valuePos list
        seen = set([0,0,0])
        while heap:
            totalSum, idxRooks1, idxRooks2, idxRooks3 = heapq.heappop(heap)
            rooks1, rooks2, rooks3 = valuePos[idxRooks1], valuePos[idxRooks2], valuePos[idxRooks3]
            totalSum = board[rooks1[1]][rooks1[2]] + board[rooks2[1]][rooks2[2]] + board[rooks3[1]][rooks3[2]]
            # Check conflict
            if rooks1[1] != rooks2[1] and rooks2[1] != rooks3[1] and rooks1[1] != rooks3[1] and rooks1[2] != rooks2[2] and rooks2[2] != rooks3[2]  and rooks1[2] != rooks3[2]: # comprarre the j and i indexes
                # not conflict
                # print(rooks1, rooks2, rooks3)
                totalSum = board[rooks1[1]][rooks1[2]] + board[rooks2[1]][rooks2[2]] + board[rooks3[1]][rooks3[2]]
                return totalSum
            else:
                # there is a conflict so we must add the new bests combinations that leads to the highest totalSum, and keep doing a bfs untill we find a pair without conflict
                if idxRooks1+1 < len(valuePos) and (idxRooks1+1, idxRooks2, idxRooks3) not in seen: 
                    rooks1_, rooks2_, rooks3_ = valuePos[idxRooks1+1], valuePos[idxRooks2], valuePos[idxRooks3]
                    totalSum = board[rooks1_[1]][rooks1_[2]] + board[rooks2_[1]][rooks2_[2]] + board[rooks3_[1]][rooks3_[2]]
                    heapq.heappush(heap, (-totalSum, idxRooks1+1, idxRooks2, idxRooks3))
                if idxRooks2+1 < len(valuePos) and (idxRooks1, idxRooks2+1, idxRooks3) not in seen: 
                    rooks1_, rooks2_, rooks3_ = valuePos[idxRooks1], valuePos[idxRooks2+1], valuePos[idxRooks3]
                    totalSum = board[rooks1_[1]][rooks1_[2]] + board[rooks2_[1]][rooks2_[2]] + board[rooks3_[1]][rooks3_[2]]
                    heapq.heappush(heap, (-totalSum, idxRooks1, idxRooks2+1, idxRooks3))
                if idxRooks3+1 < len(valuePos) and (idxRooks1, idxRooks2, idxRooks3+1) not in seen: 
                    rooks1_, rooks2_, rooks3_ = valuePos[idxRooks1], valuePos[idxRooks2], valuePos[idxRooks3+1]
                    totalSum = board[rooks1_[1]][rooks1_[2]] + board[rooks2_[1]][rooks2_[2]] + board[rooks3_[1]][rooks3_[2]]
                    heapq.heappush(heap, (-totalSum, idxRooks1, idxRooks2, idxRooks3+1))
                seen.add((idxRooks1+1, idxRooks2, idxRooks3))
                seen.add((idxRooks1, idxRooks2+1, idxRooks3))
                seen.add((idxRooks1, idxRooks2, idxRooks3+1))

        return 0

