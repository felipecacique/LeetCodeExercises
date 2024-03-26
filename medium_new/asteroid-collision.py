class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # https://leetcode.com/problems/asteroid-collision/?envType=study-plan-v2&envId=leetcode-75

        stack = []

        for a in asteroids:

            stack.append(a)

            while len(stack) > 1: # solve steroid collisions
                if  not (stack[-1] < 0 and stack[-2] > 0): # no colision: moving to the same direction or in oposite direction without colision (e.g., [-2,-1,1,2]) # (stack[-1] > 0 and stack[-2] > 0)
                    break
                elif abs(stack[-1]) > abs(stack[-2]): # they are moving in oposite directions and stack[-1] is larger than stack[-2]
                    aux = stack.pop()
                    _ = stack.pop()
                    stack.append(aux) # stack[-1] colided with stack[-2], and now stack[-1] stays on the stack
                elif abs(stack[-1]) < abs(stack[-2]):
                    _ = stack.pop() #  stack[-2] exploded  with stack[-1], so we remove stack[-1] and keep stack[-2]
                    break
                elif abs(stack[-1]) == abs(stack[-2]): # they are moving in oposite directions they have the same size
                    stack.pop()
                    stack.pop()
                    break

        return stack