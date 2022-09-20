
from math import ceil

#FUNCTIONS
def area(width, height):
    return width * height

def listArea(wallList):
    total = 0
    for i in range(len(wallList)):
        total += wallList[i].area
        #print(total)
    return total

#ERROR HANDLING, CHECK TO MAKE SURE A VALID NUMBER HAS BEEN GIVEN, OTHERWISE ASK THE USER AGAIN
def inputNum(inputMessage):
    '''
    #USING TRY AND EXCEPT INSTEAD OF IF ELSE

    numericFlag = False
    while numericFlag != True:
        try:
            tempNum = int(input(inputMessage))
            numericFlag = True
            return tempNum
        except ValueError:
            print("Please enter a valid number")
    '''
    numericFlag = False
    while numericFlag != True:
        tempNum = input(inputMessage)
        if tempNum.isnumeric():
            tempNum = int(tempNum)
            numericFlag = True
        else:
            print("Please enter a valid number\n")
    return tempNum
    
    

#ERROR HANDLING TO MAKE SURE A VALID PAINT TYPE IS CHOSEN
def paintCheck (wallNum):
    if wallNum == 0:
        paintFlag = 0
        while paintFlag == 0:
            paintType = input('What type of paint would you like to buy\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
            
            if paintType == 'regular' or paintType == 'premium' or paintType == 'diamond':
                paintFlag = 1
            else:
                print("\nPlease enter regular, premium, or diamond\n")
    else:
        paintFlag = 0
        while paintFlag == 0:
            paintType = input(f'What type of paint would you like to buy for wall {wallNum}\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
            
            if paintType == 'regular' or paintType == 'premium' or paintType == 'diamond':
                paintFlag = 1
            else:
                print("\nPlease enter regular, premium, or diamond\n")
    return paintType

#ERROR HANDLING TO MAKE SURE A VALID PAINT TYPE IS CHOSEN
def sheenCheck (wallNum):
    if wallNum == 0:
        sheenFlag = 0
        while sheenFlag == 0:
            sheenType = input('\nWhat type of sheen would you like?\nSemi-Gloss (type semi_gloss) - $6\nSatin (type satin) - $4\nFlat (type flat) - $2:\n')        
            if sheenType == 'semi_gloss' or sheenType == 'satin' or sheenType == 'flat':
                sheenFlag = 1
            else:
                print("\nPlease enter semi_gloss, satin or flat\n")
    else:
        sheenFlag = 0
        while sheenFlag == 0:
            sheenType = input(f'\nWhat type of sheen would you like for wall {wallNum}?\nSemi-Gloss (type semi_gloss) - $6\nSatin (type satin) - $4\nFlat (type flat) - $2:\n')        
            if sheenType == 'semi_gloss' or sheenType == 'satin' or sheenType == 'flat':
                sheenFlag = 1
            else:
                print("\nPlease enter semi_gloss, satin or flat\n")
    return sheenType

def paintSelection(wallNum):
    if wallNum == 0:
        print(f"\nPAINT INFO")
    else:
        print(f"\nPAINT INFO FOR WALL #{wallNum}")
    paintType = paintCheck(wallNum)
    sheenType = sheenCheck(wallNum)
    color = input(f'\nWhat color paint would you like?:\n')

    #CREATE PAINT OBJECT & PRINT INFO
    exPaint = Paint('y', paintType, sheenType, color)
    exPaint.printPaint()

    return exPaint

###########################################################################################################
#OBJECT CLASSES
class Paint:
    def __init__ (self, isExterior, type, sheen, color):
        self.isExterior = isExterior
        self.type = type
        self.sheen = sheen
        self.color = color
        #self.cost = self.findCost()

    def printPaint (self):
        print('\nYOUR PAINT INFO:')
        print(f"Color: {self.color}")
        print(f"Quality: {self.type}")
        print(f"Finish: {self.sheen}")
        if self.isExterior == 'y':
            print("In/Ex: exterior\n")
        elif self.isExterior == 'n':
            print("In/Ex: interior\n")

    #could probably just put this into costForArea function
    def findCost (self):
        cost = 0
        if self.isExterior == 'y':
            cost = 10
        paintType = {'regular': 10, 'premium': 20, 'diamond': 30}
        sheen = {'semi_gloss': 6, 'satin': 4, 'flat': 2}
        cost += paintType.get(self.type) + sheen.get(self.sheen)
        return cost
    
    def costForArea (self, area, wallNum):
        paintCost = self.findCost()

        #NUMBER OF GALLONS NEEDED TO COVER THE AREA
        numGallons = area/400
        numPrimer = 0

        if wallNum == 0:
            #ACCOUNTING FOR COATS (DIAMOND ONLY NEEDS 1)
            if self.type == 'regular':
                print(f"Your paint costs ${paintCost} per gallon + $10 per gallon of Primer")
                #IF REGULAR NEEDs PRIMER
                numPrimer = ceil(numGallons)
                #2 COATS FOR REGULAR
                numGallons = ceil(numGallons*2)
                print(f"You will need {numGallons} gallon(s) of paint")
                print(f"You will need {numPrimer} gallon(s) of primer")
            elif self.type == 'premium':
                print(f"Your paint costs ${paintCost} per gallon")
                #2 COATS FOR PRIMER
                numGallons = ceil(numGallons*2)
                print(f"You will need {numGallons} gallon(s) of paint")
            else:
                print(f"Your paint costs ${paintCost} per gallon")
                numGallons = ceil(numGallons)
                print(f"You will need {numGallons} gallon(s) of paint")
        else:
            #ACCOUNTING FOR COATS (DIAMOND ONLY NEEDS 1)
            if self.type == 'regular':
                print(f"Your paint costs ${paintCost} per gallon + $10 per gallon of Primer for wall #{wallNum}")
                #IF REGULAR NEEDs PRIMER
                numPrimer = ceil(numGallons)
                #2 COATS FOR REGULAR
                numGallons = ceil(numGallons*2)
                print(f"You will need {numGallons} gallon(s) of paint for wall #{wallNum}")
                print(f"You will need {numPrimer} gallon(s) of primer for wall #{wallNum}")
            elif self.type == 'premium':
                print(f"Your paint costs ${paintCost} per gallon for wall #{wallNum}")
                #2 COATS FOR PRIMER
                numGallons = ceil(numGallons*2)
                print(f"You will need {numGallons} gallon(s) of paint for wall #{wallNum}")
            else:
                print(f"Your paint costs ${paintCost} per gallon for wall #{wallNum}")
                numGallons = ceil(numGallons)
                print(f"You will need {numGallons} gallon(s) of paint for wall #{wallNum}")

        #EXTERIOR COST CALCULATION AND PRINT
        cost = (numGallons * paintCost) + (numPrimer * 10)
        return cost

class Wall:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = area(width, height)
        self.windowList = []
        self.doorList = []

    def addWindow(self, wallNum):
        if wallNum == 0:
            numWindows = inputNum(f'How many windows does the wall have?:\n')
            if numWindows > 0:
                for j in range(numWindows):
                    width = inputNum(f'What is the width of window #{j+1} on the wall:\n')
                    height = inputNum(f'What is the height of window #{j+1} on the wall:\n')
                    newWindow = WindowOrDoor(width, height)
                    self.windowList.append(newWindow)
                    self.area -= newWindow.area
            else:
                return
        else:
            numWindows = inputNum(f'How many windows does wall #{wallNum} have?:\n')
            if numWindows > 0:
                for j in range(numWindows):
                    width = inputNum(f'What is the width of window #{j+1} on wall #{wallNum}:\n')
                    height = inputNum(f'What is the height of window #{j+1} on wall #{wallNum}:\n')
                    newWindow = WindowOrDoor(width, height)
                    self.windowList.append(newWindow)
                    self.area -= newWindow.area
            else:
                return
        #self.windowList.append(window)
        #self.area -= window.area

    def addDoor(self, wallNum):
        if wallNum == 0:
            numDoors = inputNum(f'How many doors does the wall have?:\n')
            if numDoors > 0:
                for j in range(numDoors):
                    width = inputNum(f'What is the width of door #{j+1} on the wall:\n')
                    height = inputNum(f'What is the height of door #{j+1} on the wall:\n')
                    newDoor = WindowOrDoor(width, height)
                    
                    paintDoor = input(("Do you want to paint the door?(y/n):\n"))
                    if paintDoor == 'n':
                        self.area -= newDoor.area
                    elif paintDoor == 'y':
                        newDoor.painted = True
                        #print("Should be True")
                        #print(self.painted)
                    else:
                        print('Please enter a valid answer')

                    self.doorList.append(newDoor)
            else:
                return
        else:
            numDoors = inputNum(f'How many doors does wall #{wallNum} have?:\n')
            if numDoors > 0:
                for j in range(numDoors):
                    width = inputNum(f'What is the width of door #{j+1} on wall #{wallNum}:\n')
                    height = inputNum(f'What is the height of door #{j+1} on wall #{wallNum}:\n')
                    newDoor = WindowOrDoor(width, height)
                
                    paintDoor = input(("Do you want to paint the door?(y/n):\n"))
                    if paintDoor == 'n':
                        self.area -= newDoor.area
                    elif paintDoor == 'y':
                        newDoor.painted = True
                        #print("Should be True")
                        #print(self.painted)
                    else:
                        print('Please enter a valid answer')

                    self.doorList.append(newDoor)

            else:
                return

class WindowOrDoor:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = area(width, height)
        self.painted = False

##############################################################################################################
#MAIN
if __name__ == '__main__':
    print("Welcome to the house paint calculator!\n")
    totalArea = 0
    totalCost = 0
    outsideOrInside = ''
    exArea = 0

    while (outsideOrInside != 'o') and (outsideOrInside != 'i'):
        outsideOrInside = input('Are you planning on painting the outside (o) or the inside (i)?:\n')

#########################################################################
        #OUTSIDE
        if outsideOrInside == 'o':
            
            numOutWalls = inputNum('How many walls on the outside of the house are you painting?:\n')
            outWalls = []
            sameSize = ''

            #IF MORE THAN ONE WALL
            if numOutWalls > 1:

            #ERROR HANDLING, CHECK IF Y OR N HAS BEEN ENTERED
                while sameSize != 'y' and sameSize != 'n':
                    sameSize = input('Are the outside walls of the house the same dimensions?(y/n):\n')

                    #SAME DIMENSIONS
                    if sameSize == 'y':
                        width = inputNum('What is the width of the walls in ft?:\n')
                        height = inputNum('What is the height of the walls in ft?:\n')
                        for i in range(numOutWalls):
                            outWalls.append(Wall(width, height))
                            outWalls[i].addWindow(i+1)
                            outWalls[i].addDoor(i+1)

                    #DIFFERENT DIMENSIONS
                    elif sameSize == 'n':
                        for i in range(numOutWalls):
                            width = inputNum(f'What is the width of wall #{i+1} in ft?:\n')
                            height = inputNum(f'What is the height of wall #{i+1} in ft?:\n')
                            outWalls.append(Wall(width, height))

                            #SEE IF THERE ARE ANY WINDOWS ON THIS WALL
                            outWalls[i].addWindow(i+1)
                            #ANY DOORS ON THE WALL
                            outWalls[i].addDoor(i+1)

                    #INVALID RESPONSE
                    else:
                        print("Please enter a valid answer\n")

            #ONLY 1 WALL
            else:
                width = inputNum('What is the width of the wall in ft?:\n')
                height = inputNum('What is the height of the wall in ft?:\n')
                tempWall = Wall(width, height)
                #ADD ANY WINDOWS OR DOORS
                tempWall.addWindow(0)
                tempWall.addDoor(0)
                outWalls.append(tempWall)
            
            #FIND THE TOTAL AREA
            exArea = listArea(outWalls)
            for i in range(len(outWalls)):
                numWindows = len(outWalls[i].windowList)
                if numWindows > 0:
                    print(f"\nWall #{i+1} contains {numWindows} window(s)")
                    for j in range(numWindows):
                        print(f"Window #{j+1} is {outWalls[i].windowList[j].area} sqft in area")
                
                numDoors = len(outWalls[i].doorList)
                if numDoors > 0:
                    print(f"\nWall #{i+1} contains {numDoors} door(s)")
                    for j in range(numDoors):
                        print(f"Door #{j+1} is {outWalls[i].doorList[j].area} sqft in area")

                        if outWalls[i].doorList[j].painted == True:
                            print(f"This door will be painted, therefor it will not subtract from the total area to be painted")

                print(f"Wall #{i+1} Total Area To Paint: {outWalls[i].area} sqft\n")

            print(f"Total exterior area to be paint: {exArea} sqft\n")
            #totalArea += exArea

            ########################################
            #CHOOSE PAINT
            ########################################
            samePaint = ''
            while samePaint != 'y' and samePaint != 'n':
                samePaint = input('Do you want all the walls to have the same paint?(y/n):\n')

                #SAME PAINT
                if samePaint == 'y':
                    #SELECT PAINT
                    exPaint = paintSelection(0)
                    #FIND THE COST
                    exCost = exPaint.costForArea(exArea, 0)

                #DIFFERENT PAINT
                elif samePaint == 'n':
                    exCost = 0
                    for i in range(len(outWalls)):
                        exPaint = paintSelection(i+1)
                        tempCost = exPaint.costForArea(outWalls[i].area, i+1)
                        print(f"Wall #{i+1} will cost ${tempCost}")
                        exCost += tempCost
                else:
                    print("Please enter a valid answer")

            print(f"Your exterior paint job will cost ${exCost}\n")
            #totalCost += exCost
################################################################################################
        #INSIDE
        elif outsideOrInside == 'i':
            numInWalls = inputNum('How many walls on the inside of the house are you painting?:\n')
            inWalls = []
            sameSize = ''
            while sameSize != 'y' and sameSize != 'n':
                sameSize = input('Are the inside walls of the house the same dimensions?(y/n):\n')

                #DIFFERENT DIMENSIONS
                if sameSize == 'y':
                    width = inputNum(f'What is the width of the walls in ft?:\n')
                    height = inputNum(f'What is the height of the walls in ft?:\n')
                    for i in range(numInWalls):
                        inWalls.append(Wall(width, height))


                #SAME DIMENSIONS
                elif sameSize == 'n':
                    for i in range(numInWalls):
                        width = inputNum(f'What is the width of wall #{i+1} in ft?:\n')
                        height = inputNum(f'What is the height of wall #{i+1} in ft?:\n')
                        inWalls.append(Wall(width, height))

                #INVALID RESPONSE
                else:
                    print("Please enter a valid answer\n")
            
            inArea = listArea(inWalls)
            print(f"Interior Area to be painted: {inArea} sqft\n")
            #totalArea += inArea

            ####################################
            #CHOOSE PAINT
            ####################################
            samePaint = ''
            while samePaint != 'y' and samePaint != 'n':
                samePaint = input('Do you want all the walls to have the same paint?(y/n):\n')
                #SAME PAINT
                if samePaint == 'y':
                    #SELECT PAINT
                    inPaint = paintSelection(0)
                    #FIND THE COST
                    inCost = inPaint.costForArea(inArea, 0)

                #DIFFERENT PAINT
                elif samePaint == 'n':
                    inCost = 0
                    for i in range(len(inWalls)):
                        inPaint = paintSelection(i+1)
                        tempCost = inPaint.costForArea(inWalls[i].area, i+1)
                        print(f"Wall #{i+1} will cost ${tempCost}")
                        inCost += tempCost
                else:
                    ("Please enter a valid answer")

                print(f"\nYour interior paint job will cost ${inCost}\n")
        else:
            print("Please enter a valid answer")