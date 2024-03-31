class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # https://leetcode.com/problems/reorder-data-in-log-files/
        arrLetter = []
        arrDigits = []
        
        for log in logs:
            arr = log.split()
            if arr[1][0] in ['0','1','2','3','4','5','6','7','8','9'] :
                arrDigits.append(log)
            else:
                invertedLogArr = (arr[1:],arr[0:1])
                arrLetter.append(invertedLogArr)
                
        arrLetter = sorted(arrLetter)
        for i,arr in enumerate(arrLetter):
            new_arr = arr[1]+arr[0]
            log = " ".join(new_arr)
            arrLetter[i] = log
        
        return arrLetter + arrDigits