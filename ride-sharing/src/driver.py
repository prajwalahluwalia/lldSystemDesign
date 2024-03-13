from collections import defaultdict

class Driver:
    def __init__(self):
        self.drivers = defaultdict(dict)
        self.occupiedDrivers = defaultdict()
        
    def addDriver(self, id, xPos, yPos):
        if id in self.drivers:
            return f"Driver already added."
        
        self.drivers[id] = {'xPos': xPos, 'yPos': yPos}
        
        return f'Driver added.'
        
    def getDrivers(self):
        return self.drivers
    
    def getOccupiedDrivers(self):
        return self.occupiedDrivers
    
    def addToOccupiedDrivers(self, driverId, rideId):
        self.occupiedDrivers[driverId] = rideId
        
    def removeOccupiedDriver(self, driverId):
        del self.occupiedDrivers[driverId]