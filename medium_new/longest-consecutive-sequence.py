class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        def Solution1(): # works efficiently, but very complicated and long to implement
            if nums == []:
                return 0

            sequences = [] # [ (start, end, size) ... ]
            complementSequence = {} # n: index_in_sequences_which_n_is_part_of , with the complements
            seen = set()
            for num in nums:

                if num in seen:
                    continue
                seen.add(num)

                if num in complementSequence:
                    
                    # num is a complement of some sequence in sequences, might add to the sequence from the left of frrom the right
                    # if it merges with 2 
                    ids = complementSequence[num]
                    
                    if len(ids)>1: # it merges with 2 sequences
                        complementSequence.pop(num)
                        # merge the sequences
                        i = ids[0]
                        starti, endi, counti = sequences[i]
                        j = ids[1]
                        startj, endj, countj = sequences[j]
                        # add num to this sequence and merge both
                        if starti < startj:
                            start = starti
                            end = endj
                            count = counti + countj
                            ids_ = complementSequence.pop(end)
                            for i_ in range(len(ids_)):
                                if ids_[i_] == j:
                                    ids_[i_] = i
                            complementSequence[end] = ids_

                        else:
                            start = startj
                            end = endi
                            count = counti + countj
                            ids_ = complementSequence.pop(start-1)
                            for i_ in range(len(ids_)):
                                if ids_[i_] == j:
                                    ids_[i_] = i
                            complementSequence[start-1] = ids_
                    
                        sequences[i] = [start, end, count+1]
    

                    else:
                        complementSequence.pop(num)
                        i = ids[0]
                        start, end, count = sequences[i]
                        # add num to this sequence
                        if num < start:
                            # complementSequence.pop(start-1)
                            start = num
                            complementSequence[start-1] = complementSequence.get(start-1,[]) +  [i]
                            
                        elif num == end:
                            # complementSequence.pop(end)
                            end = num + 1
                            complementSequence[end] = complementSequence.get(end,[]) + [i]
            
                        sequences[i] = [start,end,count+1]
                        
                else: # this number is not part of any sequence, so we will start a new sequence from it
                    sequences.append([num,num+1,1])
                    complementSequence[num-1] = complementSequence.get(num-1,[]) + [len(sequences) - 1]
                    complementSequence[num+1] = complementSequence.get(num+1,[]) + [len(sequences) - 1]

            sequences = sorted(sequences, key=lambda x: x[2])

            return sequences[-1][2]

        def Solution2():
            # i use one of th solutions from the proproblem, and i find this very good. The main point is not to do the lookup loop for nums that is in the middle of a sequence, only for nums that is the start of the sequence.
            if not nums: return 0

            max_len = 0
            unique = set()
            for num in nums:
                unique.add(num)

            for num in unique:
                if num-1 in unique: # KEY! num is in the middle of some sequence, so we will not do the look up. It is here that we transform this algorithm that is o(n^2) in o(n)
                    continue
                else: # num is the start of some sequence. The number of lookups is equal to the size of the sequence. So the totol number of looups for the entire preocess is O(n), since not a single num is has to be looked twice
                    curr_len = 1
                    numAux = num
                    while numAux + 1 in unique:
                        curr_len += 1
                        numAux += 1
                max_len = max(max_len, curr_len)

            return max_len

        return Solution2()
