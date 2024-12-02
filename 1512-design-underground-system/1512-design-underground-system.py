class UndergroundSystem:

    def __init__(self):
        self.path = defaultdict(lambda: {})
        self.checked = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.checked:
            print("ERROR")
            return None

        self.checked[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checked:
            print("ERROR")
            return None

        start, start_time = self.checked[id]
        del self.checked[id]

        if stationName not in self.path[start]:
            self.path[start][stationName] = (0, 0)

        cur_sum, cur_num = self.path[start][stationName]
        cur_sum += t - start_time
        cur_num += 1
        self.path[start][stationName] = (cur_sum, cur_num)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if endStation not in self.path[startStation]:
            self.path[startStation][endStation] = (0, 0)

        cur_sum, cur_num = self.path[startStation][endStation]
        return cur_sum / cur_num


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)