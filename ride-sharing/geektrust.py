from sys import argv
from src.ride import Ride
from src.driver import Driver
from src.rider import Rider

def main():    
    inputs = [[
        'ADD_DRIVER D1 1 1',
        'ADD_DRIVER D2 4 5',
        'ADD_DRIVER D3 2 2',
        'ADD_RIDER R1 0 0',
        'MATCH R1',
        'START_RIDE RIDE-001 2 R1',
        'STOP_RIDE RIDE-001 4 5 32',
        'BILL RIDE-001'
    ],[
        'ADD_DRIVER D1 0 1',
        'ADD_DRIVER D2 2 3',
        'ADD_RIDER R1 3 5',
        'ADD_DRIVER D3 4 2',
        'ADD_RIDER R2 1 1',
        'MATCH R1',
        'MATCH R2',
        'START_RIDE RIDE-101 1 R1',
        'START_RIDE RIDE-102 1 R2',
        'STOP_RIDE RIDE-101 10 2 48',
        'STOP_RIDE RIDE-102 7 9 50',
        'BILL RIDE-101',
        'BILL RIDE-102'
    ]]
    
    for values in inputs:
        driver = Driver()
        rider = Rider(driver)
        ride = Ride(rider, driver)

        for input in values:
            action = input.split()
            if action[0]=='ADD_DRIVER':
                print(driver.addDriver(action[1], int(action[2]), int(action[3])))

            elif action[0]=='ADD_RIDER':
                print(rider.addRider(action[1], int(action[2]), int(action[3])))
                
            elif action[0]=='MATCH':
                print(rider.matchToDriver(action[1]))
            
            elif action[0]=='START_RIDE':
                print(ride.startRide(action[1], int(action[2]), action[3]))
                
            elif action[0]=='STOP_RIDE':
                print(ride.stopRide(action[1], int(action[2]), int(action[3]), int(action[4])))
                
            elif action[0]=='BILL':
                print(ride.bill(action[1]))
                
            
if __name__ == "__main__":
    main()