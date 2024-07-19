class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150

        def fillNewLine(start, end, charsWithoutSpace, lastLine):
            amountWords = end - start
            amountSpaces = amountWords - 1
            totalSizeSpaces = maxWidth - charsWithoutSpace
            a = totalSizeSpaces // amountSpaces if amountSpaces!= 0 else None
            r = totalSizeSpaces % amountSpaces if amountSpaces!= 0 else None
            if lastLine: a, r = 1, 0
            line = ""
            for i in range(start,end):
                line += words[i]
                if i != end - 1 and a is not None: 
                    if r > 0:
                        line += " " * (a+1) 
                        r -= 1
                    else:
                        line += " " * a

            if len(line) < maxWidth: # to fill the empty spaces in the last line
                line += " " * (maxWidth-len(line)) 

            return line

        output = []
        chars = 0
        start = 0
        for i in range(len(words)):
            if chars + len(words[i]) > maxWidth:
                output.append(fillNewLine(start,i, chars-(i-1+1 - start), False))
                start = i
                chars = 0
            
            chars += len(words[i]) + 1 # the space

            if chars != 0 and i == len(words)-1: # to handle the last line
                output.append(fillNewLine(start,i+1, chars-(i + 1 - start), True))

        return output
