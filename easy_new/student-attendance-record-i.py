class Solution:
    def checkRecord(self, s: str) -> bool:
        # https://leetcode.com/problems/student-attendance-record-i/
        a_count = 0
        l_sequence = 0
        
        for c in s:
            if c == "A": 
                a_count += 1
            if a_count>=2: 
                return False
            
            if c == "L": 
                l_sequence += 1
            else:
                l_sequence = 0
            if l_sequence >=3:
                return False
        
        return True