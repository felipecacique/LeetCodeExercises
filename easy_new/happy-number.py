class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        cycle = False
        number = n

        while not cycle:
            seen.add(number)
            if number == 1:
                return True

            next_num = 0
            while number > 0:
                digit = number % 10
                next_num += digit ** 2
                number = number // 10
            number = next_num

            # digits = list(str(number))
            # number = sum([int(digit)**2 for digit in digits])
            
            if number in seen:
                cycle = True

        return False