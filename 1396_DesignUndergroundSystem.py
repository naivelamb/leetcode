"""
https://leetcode.com/problems/design-underground-system/

Use two hash tables.
Hash table 1, key: customer id, value = [start_station, start_time]
Hash table 2, key: (start_station, end_station), value = [total_travel_time, total_customer]

When CheckIn, create a new key-value pair in hash table 1.
When checkOut, find the value in hash table 1, use the value to compute (start_station, end_station) and travel time, add to hash table 2. Remove the record from hash table 1.
"""
class UndergroundSystem:

    def __init__(self):
        self.customer = {}
        self.station = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_start, t_start = self.customer[id]
        del self.customer[id]
        if (station_start, stationName) in self.station:
            self.station[(station_start, stationName)][0] += t - t_start
            self.station[(station_start, stationName)][1] += 1
        else:
            self.station[(station_start, stationName)] = [t - t_start, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station[(startStation, endStation)][0]/self.station[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)