class TimeMap:
    def __init__(self):
        self.timeMap = defaultdict(list)    # key -> [[ts, val], ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.timeMap[key])
        if n == 0:
            return ""

        l, r = 0, n - 1
        res = ""
        pair = self.timeMap[key]

        while l <= r:
            m = (r - l) // 2 + l

            if pair[m][0] <= timestamp: 
                res = pair[m][1]
                l = m + 1
            else:
                r = m - 1

        return res




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)