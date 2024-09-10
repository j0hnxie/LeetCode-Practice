class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        else:
            timestamps = self.keys[key]

            if timestamp < timestamps[0][0]:
                return ""

            l, r = 0, len(timestamps)
            while l < r:
                m = l + (r - l) // 2
                if timestamp >= timestamps[m][0]:
                    l = m + 1
                else:
                    r = m
            return timestamps[m][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)