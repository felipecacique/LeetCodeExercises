# https://leetcode.com/problems/trapping-rain-water/

# solution4() and solution5() are te best solution time O(n)
    
class Solution:
    def trap(self, height: List[int]) -> int:
        
        def Solution1(height):
            # time O(nlogn)

            unique = set(height)
            unique = list(unique)
            unique.sort()

            # m = max(height)
            # unique = range(0,m+1)

            total_volume = 0

            for j, u in enumerate(unique):
                
                start_counting = False
                pseudo_volume = 0

                for i, h in enumerate(height):
                    
                    if h >= u:
                        start_counting = True
                        total_volume += pseudo_volume
                        pseudo_volume = 0

                    if start_counting == True:
                        if h < u: 
                            pseudo_volume += unique[j] - unique[j-1]
        
            return total_volume


        def Solution2(height):
            
            # use a stack/queue

            stack = []

            max_height = 0
            black = 0
            total_volume = 0

            for i, h in enumerate(height):
                
                if h != 0:
                    stack.append((h,i))
                
                    if len(stack) > 1:
                        
                        # compute water
                        water_black = min(stack[-1][0], stack[-2][0]) * (stack[-1][1] - stack[-2][1] -1) 
                        # water = min(stack[-1][0], stack[-2][0]) * (stack[-1][1] - stack[-2][1] -1)
                        # black_water = min(stack[-1][0], stack[-2][0]) * (stack[-1][1] - stack[-2][1] +1)
                        water = water_black - black
                        
                        print(stack, water_black, black, water, total_volume)
                        
                        if stack[-1][0] <= stack[-2][0]:
                            black += stack[-1][0]
                            del stack[-1]
                        else:
                            # the last added to the pile is highest
                            # reset some variables
                            black = 0
                            total_volume += water

                    

            return total_volume
        
        def Solution3(height):
            
            # use a stack/queue

            stack = [(0,-1)]

            max_height = 0
            black = 0
            total_volume = 0
          
            for i, h in enumerate(height):
                
                if h != 0:

                    # compute water
                    water_black = min(h, stack[-1][0]) * (i - stack[-1][1] -1) 
                    # water = min(stack[-1][0], stack[-2][0]) * (stack[-1][1] - stack[-2][1] -1)
                    # black_water = min(stack[-1][0], stack[-2][0]) * (stack[-1][1] - stack[-2][1] +1)
                    water = water_black - black

                    total_volume += max(water,0)
                    
                    print((i,h), stack, water_black, black, water, total_volume)
                    
                    if h <= stack[-1][0]:
                        black += h
                        
                    else:
                        # the last added to the pile is highest
                        # reset some variables
                        stack.append((h,i))
                        black = 0
                        repeated_water = 0
                        

                    

            return total_volume


        def Solution4(height):
             # using left and right pointers, similar to https://www.youtube.com/watch?v=ZI2z5pq0TqA&ab_channel=NeetCode . Time O(n)

            left = 0
            right = len(height)-1
            max_left = left
            max_right = right

            water = 0

            while left < right:

                if height[left] > height[max_left]:
                    max_left = left
                
                if height[right] > height[max_right]:
                    max_right = right  

                if height[right] < height[max_left]:
                    water += min(height[max_left], height[max_right]) - height[right]
                    right -= 1
                else:
                    water += min(height[max_left], height[max_right]) - height[left]
                    left += 1

            return water       


        def Solution5(height):
            # using left and right pointers, similar to https://www.youtube.com/watch?v=ZI2z5pq0TqA&ab_channel=NeetCode . Time O(n)
            # it is the same as the solution 4, but with less ifs, more similar to the netcode's 
            left = 0
            right = len(height)-1
            max_left = height[left]
            max_right = height[right]

            water = 0

            while left < right:

                if height[right] < max_left:
                    right -= 1
                    max_right = max(max_right, height[right])
                    water += max_right - height[right]
                    
                else:
                    left += 1
                    max_left = max(max_left, height[left])
                    water += max_left - height[left]
                    
            return water  
        
        return Solution5(height)