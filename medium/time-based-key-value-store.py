# https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.d = {}
        self.key_last_timestamp = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if not timestamp in self.d:
            self.d[timestamp] = {key: value}
        else:
            if not key in self.d[timestamp]:
                self.d[timestamp][key] = value
            else:
                self.d[timestamp][key] = value # replace the value

        if not key in self.key_last_timestamp:
            self.key_last_timestamp[key] = [timestamp]
        else:
            self.key_last_timestamp[key].append(timestamp) # holds the last timestamps for a key


    def get(self, key: str, timestamp: int) -> str:
        
        last_timestamp = None
        if key in self.key_last_timestamp:
            for i in range(len(self.key_last_timestamp[key])-1, -1, -1):
                if timestamp >= self.key_last_timestamp[key][i]:
                    last_timestamp = self.key_last_timestamp[key][i]
                    break

        if last_timestamp:
            if last_timestamp in self.d:
                if key in self.d[last_timestamp]:
                    return self.d[last_timestamp][key]
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)