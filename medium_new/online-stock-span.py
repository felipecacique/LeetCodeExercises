class StockSpanner:
    # https://leetcode.com/problems/online-stock-span/?envType=study-plan-v2&envId=leetcode-75
    # simular to daily-temperatures
    def __init__(self):
        self.stack = [(float('inf'), 0)]
        self.i = 1
        

    def next(self, price: int) -> int:
        # monotonic stack

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        if self.stack:
            countSmallerThanPrice = self.i - self.stack[-1][1]
            
        self.stack.append((price, self.i))

        self.i += 1

        return countSmallerThanPrice
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)