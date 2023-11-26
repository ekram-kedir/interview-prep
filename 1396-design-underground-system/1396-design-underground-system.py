class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} #id -> (startstation , times)
        self.totalMap = {} #(start, end) -> [totalTime, count]
        
    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkInMap[id] = (startStation, t)

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        start, time = self.checkInMap[id]
        path = (start , endStation)
        if path not in self.totalMap:
            self.totalMap[path] = [0, 0]
        self.totalMap[(start, endStation)][0] += t - time
        self.totalMap[(start, endStation)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total/count
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)