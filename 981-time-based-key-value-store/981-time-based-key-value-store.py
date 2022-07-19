class TimeMap:
    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dict.get(key) is not None:
            self.dict[key].append((value, timestamp))
        else:
            self.dict[key] = [(value, timestamp)]
            
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if self.dict.get(key) is not None:
            time_series = self.dict.get(key)
            l, r = 0, len(time_series) - 1
            while l <= r:
                m = (l+r) // 2
                if timestamp >= time_series[m][1]:
                    res = time_series[m][0]
                    l = m + 1
                else:
                    r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)