# https://leetcode.com/problems/implement-queue-using-stacks/submissions/1093068973/


class MyQueue:
    def __init__(self):
        self.array = []

    def push(self, x: int) -> None:
        self.array.append(x)

    def pop(self) -> int:
        return self.array.pop(0)

    def peek(self) -> int:
        return self.array[0]

    def empty(self) -> bool:
        return True if len(self.array) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
