class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # https://leetcode.com/problems/invalid-transactions/
        # O(60*n) = O(n)
        
        h = {}
        nameCity = {}
        for i in range(len(transactions)):
            t = transactions[i].split(",")
            h[(t[0], t[1])] = i
            nameCity[(t[0], t[1])] = nameCity.get((t[0], t[1]), []) + [t[3]]
        
        output = []
        for i in range(len(transactions)):
            t = transactions[i].split(",")
            if int(t[2]) > 1000:
                output.append(transactions[i])
                continue
            
            flagBreak = False
            for timeDelta in range(-60, 60):
                if (t[0], str(int(t[1])+timeDelta)) in h:
                    for city in nameCity[(t[0], str(int(t[1])+timeDelta))]:
                        if city != t[3]:
                            output.append(transactions[i])
                            flagBreak = True
                            break
                    if flagBreak: break
                    
        return output
            