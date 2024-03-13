import math
from src.driver import Driver
from collections import defaultdict

class Rider:
    def __init__(self, driverInstance):
        self.riders = defaultdict(dict)
        self.drivers = driverInstance
        
    def addRider(self, id, xPos, yPos):
        if id in self.riders:
            return f'Rider already exists.'
        
        self.riders[id] = {'xPos':xPos, 'yPos':yPos}
        return f'Rider added.'
        
    def matchToDriver(self, riderId):
        if riderId not in self.riders:
            return f"INVALID_RIDER"
        else:
            try:               
                availDrivers = self.getAvailableDrivers(riderId)
                
                return f"DRIVERS_MATCHED {' '.join(availDrivers[:5])}"
            
            except Exception as e:
                return f"{e}"
            
    def getAvailableDrivers(self, riderId):
        try:
            xPos = self.riders[riderId]['xPos']
            yPos = self.riders[riderId]['yPos']
                    
            nearestDrivers = defaultdict(list)     
            drivers = self.drivers.getDrivers()
            for driver in drivers:
                if driver not in self.drivers.getOccupiedDrivers():
                    dis = self.distanceToDriver(xPos, yPos, drivers[driver]['xPos'], drivers[driver]['yPos'])
                    if dis<=5:
                        nearestDrivers[dis].append(driver)
                        nearestDrivers[dis].sort()
                    
            availDrivers = []
            values = sorted(nearestDrivers.items(), key=lambda x:x[0])
            
            for value in values:
                if len(availDrivers)>=5:
                    break
                else:
                    availDrivers.extend(value[1])
                    
            return availDrivers
                    
        except Exception as e:
            return f"{e}"                    

    def distanceToDriver(self, xR, yR, xD, yD):
        try:
            return math.ceil(math.sqrt((xD-xR)**2 + (yD-yR)**2))
        except Exception as e:
            return f'{e}'
    
    def getRiders(self):
        return self.riders