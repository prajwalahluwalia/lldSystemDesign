from src.rider import Rider
from src.driver import Driver
from collections import defaultdict
import math

class Ride:
    def __init__(self, riderInstance, driverInstance):
        self.pendingRides = defaultdict(list)
        self.completedRides = defaultdict(list)
        # self.occupiedDrivers = defaultdict(dict)
        self.riders = riderInstance
        self.drivers = driverInstance
        
    def startRide(self, rideId, n, riderId):
        
        availDrivers = self.riders.getAvailableDrivers(riderId)

        if len(availDrivers)<n or availDrivers[n-1] in self.drivers.getOccupiedDrivers():
            return f"Driver is not available."
        
        if riderId not in self.riders.getRiders():
            return f"Rider does not exists."
        
        if rideId in self.pendingRides:
            return f"Invalid Ride."
        
        self.drivers.addToOccupiedDrivers(availDrivers[n-1], riderId)
        self.pendingRides[rideId]= {'driverId': availDrivers[n-1],'riderId': riderId}
        
        return f"RIDE_STARTED {rideId}"
            
    def stopRide(self, rideId, xDes, yDes, timeTaken):
        try:
            if rideId not in self.pendingRides or timeTaken<0:
                return f"INVALID_RIDE"
                
            riderId = self.pendingRides[rideId]['riderId']
            
            riders = self.riders.getRiders()
            for id in riders:
                if id==riderId:
                    distance = round(((yDes-riders[id]['yPos'])**2 + (xDes-riders[id]['xPos'])**2)**0.5, 2)
                    bill = self.geneateBill(distance, timeTaken)
                    
                    self.pendingRides[rideId]['bill']=bill
                    
                    self.completedRides[rideId] = self.pendingRides[rideId]
                    
                    self.drivers.removeOccupiedDriver(self.pendingRides[rideId]['driverId'])
                    del self.pendingRides[rideId]

                    return f"RIDE_STOPPED {rideId}"
                
            return f"INVALID_RIDER"
        
        except Exception as e:
            return f"{e}"
            
    def bill(self, rideId):
        if rideId not in self.completedRides and rideId not in self.pendingRides:
            return 'INVALID_RIDE'
        
        if rideId in self.pendingRides:
            return 'RIDE_NOT_COMPLETED'
        
        return f"{rideId} {self.completedRides[rideId]['driverId']} {self.completedRides[rideId]['bill']}"
            
    
    def geneateBill(self, distance, timeTaken):
        s = 50 + 6.5*distance + 2*timeTaken
        s+=(s*0.2)
        return round(s,2)