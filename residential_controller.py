elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1

class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = _id
        self.status = "0"
        self.amountOfFloors = _amountOfFloors
        self.amountOfElevators = _amountOfElevators
        self.elevatorList = []
        self.callButtonList = []

        self.createElevators(_amountOfFloors, _amountOfElevators)
        self.createCallButtons(_amountOfFloors)

    def createCallButtons(self, _amountOfFloors):
        buttonFloor = 1
        global callButtonID
        for x in range (_amountOfFloors):
            if (buttonFloor < _amountOfFloors):
                callUpButton = CallButton(callButtonID, buttonFloor, "up")
                self.callButtonList.append(callUpButton)
                callButtonID += 1
            if (buttonFloor > 1):
                callDownButton = CallButton(callButtonID, buttonFloor, "down")
                self.callButtonList.append(callDownButton)
                callButtonID += 1
            buttonFloor += 1

    def createElevators(self, _amountOfFloors, _amountOfElevators):
        global elevatorID
        for x in range (_amountOfElevators):
            elevator = Elevator(elevatorID, _amountOfFloors)
            self.elevatorList.append(elevator)
            elevatorID += 1
    
    def requestElevator(self, floor, direction):
        elevator = self.findElevator(floor, direction)
        elevator.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()

        return elevator
    
    def findElevator(self, requestedfloor, requestedDirection):
        bestElevatorInformations = {
            "bestElevator": None,
            "bestScore": 5,
            "referenceGap": 10000000
        }
        for elevator in self.elevatorList:
            if (requestedfloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedfloor)
            elif (requestedfloor > elevator.currentFloor and elevator.direction == "up" and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedfloor)
            elif (requestedfloor < elevator.currentFloor and elevator.direction == "down" and requestedDirection == elevator.direction):
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedfloor)
            elif (elevator.status == "idle"):
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedfloor)
            else:
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedfloor)
        return bestElevatorInformations["bestElevator"]

    def checkIfElevatorIsBetter(self, scoreToCheck, newElevator, bestElevatorInformations, floor):
        if (scoreToCheck < bestElevatorInformations["bestScore"]):
            bestElevatorInformations["bestScore"] = scoreToCheck
            bestElevatorInformations["bestElevator"] = newElevator
            bestElevatorInformations["referenceGap"] = abs(newElevator.currentFloor - floor)
        elif (bestElevatorInformations["bestScore"] == scoreToCheck):
            gap = abs(newElevator.currentFloor - floor)

            if (bestElevatorInformations["referenceGap"] > gap):
                bestElevatorInformations["bestScore"] = scoreToCheck
                bestElevatorInformations["bestElevator"] = newElevator
                bestElevatorInformations["referenceGap"] = gap
        
        return bestElevatorInformations


        


class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = ""
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = 1
        self.direction = None
        self.door = Door(_id)
        self.floorRequestButtonList = []
        self.floorRequestList = []

        self.createFloorRequestButtons(_amountOfFloors); 

    def createFloorRequestButtons(self, _amountOfFloors):
        buttonFloor = 1
        global floorRequestButtonID
        for x in range (_amountOfFloors):
            floorRequestButton = FloorRequestButton(floorRequestButtonID, buttonFloor)
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor += 1
            floorRequestButtonID += 1


    def requestFloor(self, floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()

    def move(self):
        while (len(self.floorRequestList)):
            destination = self.floorRequestList[0]
            screenDisplay = 0
            self.status = "moving"
            if (self.currentFloor < destination):
                self.direction = "up"
                self.sortFloorList()
                while (self.currentFloor < destination):
                    self.currentFloor += 1
                    screenDisplay = self.currentFloor
            elif (self.currentFloor > destination):
                self.direction = "down"
                self.sortFloorList()
                while (self.currentFloor > destination):
                    self.currentFloor -= 1
                    screenDisplay = self.currentFloor
            self.status = "stopped"
            self.floorRequestList.pop(0)  
        self.status = "idle"                  

    def sortFloorList(self):
        if (self.direction == "up"):
            self.floorRequestList.sort()
        else: 
            self.floorRequestList.sort(reverse=True)

    def operateDoors(self):
        # door =  Door()
        self.door.status = "opened"

class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        self.floor = _floor
        self.direction = _direction
        self.status = ""

class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.floor = _floor
        self.status = ""

class Door:
    def __init__(self, _id):
        self.ID = _id
        self.status = "closed"
        self.obstruction = None