class Solution:
    def countBits(self, n: int) -> List[int]:
        # https://leetcode.com/problems/counting-bits/?envType=study-plan-v2&envId=leetcode-75
        def Solution1():
            bits_count = [0] * (n + 1)

            for i in range(1, n + 1):
                num = i
                for _ in range(32):
                    bits_count[i] += num & 1
                    num = num >> 1

            return bits_count

        def Solution2():
            # faster
            ans = []
            for i in range(n+1):
                ans.append(bin(i).count('1'))
            return ans

        return Solution2()
