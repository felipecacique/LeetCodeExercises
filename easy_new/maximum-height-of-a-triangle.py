class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # https://leetcode.com/problems/maximum-height-of-a-triangle/description/
        sols = []
        for greatter, smaller in [(red, blue), (blue, red)]:
            sol = 1
            for i in range(101):
                levelBalls = i + 1
                if i % 2 == 0:
                    if greatter - levelBalls >= 0:
                        greatter -= levelBalls
                        sol = i + 1
                    else:
                        break
                else:
                    if smaller - levelBalls >= 0:
                        smaller -= levelBalls
                        sol = i + 1
                    else:
                        break
                sols.append(sol)
        
        return max(sols)