# https://leetcode.com/problems/add-binary/description/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        size_a = len(a)
        size_b = len(b)
        solution = ""
        vai_1 = 0

        # make them have the same size
        if size_a > size_b:
            b = (size_a - size_b) * "0" + b
        elif size_b > size_a:
            a = (size_b - size_a) * "0" + a

        print(a, b)

        for i in range(1, len(a) + 1):
            if a[-i] == "0" and b[-i] == "0" and vai_1 == 0:
                solution = "0" + solution
                vai_1 = 0

            elif a[-i] == "0" and b[-i] == "1" and vai_1 == 0:
                solution = "1" + solution
                vai_1 = 0

            elif a[-i] == "1" and b[-i] == "0" and vai_1 == 0:
                solution = "1" + solution
                vai_1 = 0

            elif a[-i] == "1" and b[-i] == "1" and vai_1 == 0:
                solution = "0" + solution
                vai_1 = 1

            elif a[-i] == "0" and b[-i] == "0" and vai_1 == 1:
                solution = "1" + solution
                vai_1 = 0

            elif a[-i] == "0" and b[-i] == "1" and vai_1 == 1:
                solution = "0" + solution
                vai_1 = 1

            elif a[-i] == "1" and b[-i] == "0" and vai_1 == 1:
                solution = "0" + solution
                vai_1 = 1

            elif a[-i] == "1" and b[-i] == "1" and vai_1 == 1:
                solution = "1" + solution
                vai_1 = 1

        if vai_1 == 1:
            solution = "1" + solution

        return solution
