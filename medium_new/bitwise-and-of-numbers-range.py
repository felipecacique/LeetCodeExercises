class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # https://leetcode.com/problems/bitwise-and-of-numbers-range/?envType=study-plan-v2&envId=top-interview-150
        # there is a rule for find out if the x-th bit of an interval bitwise is 0 or 1. 

        def solution1():
            output = 0
            for bit in range(31, -1, -1):
                # apply rule 
                s = 2**bit
                x = left//s
                y = right//s
                bitValue = x == y and x&1==1
                output = output << 1 # shift everyone to the left
                output = output | bitValue # add the bitValue to the right
            return output
    
        def Solution2(): # it is the same as the solution1, but with some optimizations
            if right == 0: return 0
            
            import math
            numberBits = int(math.log(right) / math.log(2)) # calcualte the significative number of bits. Its faster than using 32 (iterating over all bits)
            output = 0
            s = 2**numberBits
            for bit in range(numberBits, -1, -1): # we dont need to iterate over the 32 bits. We calculate the number of significant bits numberBits and just iterate over those. It makes the code faster
                # apply rule 
                x = left//s
                y = right//s
                s = s//2
                bitValue = x == y and x&1==1
                output = output << 1 # shift everyone to the left
                output = output | bitValue # add the bitValue to the right
                
            return output
       
       
        return Solution2()
       

       
        # def getBitwise(bit):
        #     # bit = #0 => s = 2^0 = 1
        #     # bit = #1 => s = 2^1 = 2
        #     # bit = #2 => s = 2^2 = 4

        #     s = 2**bit
        #     x = left//s
        #     y = right//s
        #     # if x == y and x%2==1: # odd
        #     if x == y and x&1==1: # odd
        #         # it means that the #bit of the output is 1, otherwise is 0
        #         return 1
        #     else:
        #         return 0

        # output = 0
        # for bit in range(31, -1, -1):
        #     bitValue = getBitwise(bit)
        #     output = output << 1 # shift everyone to the left
        #     output = output | bitValue # add the bitValue to the right

        # return output






        # ans = left
        # for num in range(left+1,right+1):
        #     new_ans = 0
        #     print(ans)
        #     for _ in range(32):

        #         ans_bit = ans & 1 
        #         ans = ans >> 1 

        #         num_bit = num & 1
        #         num = num >> 1

        #         if ans_bit == num_bit:
        #             new_ans = new_ans | (1) 
        #             new_ans = new_ans >> 1
        #         else:
        #             new_ans = new_ans >> 1
        #     ans = new_ans
        # return ans