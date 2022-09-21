from math import ceil

#FUNCTIONS
#finds area of a rectangle
def area(width, height):
    return width * height

#finds the area given a list of objects with an area attribute
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

#SELECT PAINT TYPE, SHEEN TYPE AND COLOR FOR ONE TYPE OF PAINT
def paintSelection(wallNum, isExterior):
    paintType = paintCheck(wallNum)
    sheenType = sheenCheck(wallNum)
    color = input(f'\nWhat color paint would you like?:\n')

    #CREATE PAINT OBJECT & PRINT INFO
    exPaint = Paint(isExterior, paintType, sheenType, color)
    if wallNum == 0:
        print(f"\nPAINT INFO")
    else:
        print(f"\nPAINT INFO FOR WALL #{wallNum}")
    exPaint.printPaint()

    return exPaint

#CHOOSE PAINT FOR EVERY WALL AND FIND COST
def choosePaint(area, wallList, numWalls, isExterior):
    cost = 0
    if numWalls > 1:
        samePaint = ''
        while samePaint != 'y' and samePaint != 'n':
            samePaint = input('Do you want all the walls to have the same paint?(y/n):\n')

            #SAME PAINT
            if samePaint == 'y':
                #SELECT PAINT
                paint = paintSelection(0, isExterior)
                #FIND THE COST
                cost = paint.costForArea(area, 0)

            #DIFFERENT PAINT
            elif samePaint == 'n':
                cost = 0
                paintList = []
                #LOOP THROUGH EACH WALL ASKING WHAT PAINT TO USE
                for i in range(len(wallList)):
                    if i > 1:
                        #IF MORE THAN 2 KINDS OF PAINT ASK IF THEY WANT TO REUSE ANOTHER KIND
                        useSamePaint = ''
                        while useSamePaint != 'y' and useSamePaint != 'n':
                            useSamePaint = input(f"\nWould you like to use a paint you have already chosen for wall #{i+1}?(y/n):\n")
                            
                            #IF THEY WANT TO USE THE SAME PAINT
                            if useSamePaint == 'y':
                                #PRINT THE PAINT LIST
                                for j in range(len(paintList)):
                                    print(f"\nPAINT #{j+1}")
                                    paintList[j].printPaint()

                                #ASK THE USER WHICH PAINT THEY WANT TO REUSE
                                paintFlag = False
                                while paintFlag != True:
                                    paintNum = inputNum(f"Which paint number would you like to use for wall #{i+1}?(1, 2, 3 ...):\n")
                                    #CHECK IF IT IS A VALID PAINT NUMBER
                                    if paintNum > len(paintList):
                                        print('Please enter a valid paint number')
                                    else:
                                        #IF IT IS A VALID NUMBER, ASSIGN THE CURRENT PAINT TYPE TO THE REQUESTED NUMBER AND PRINT
                                        paint = paintList[paintNum - 1]
                                        print(f"\nPAINT INFO FOR WALL #{i+1}")
                                        paint.printPaint()
                                        tempCost = paint.costForArea(wallList[i].area, i+1)
                                        print(f"Wall #{i+1} will cost ${tempCost}")
                                        cost += tempCost
                                        paintFlag = True

                            #IF THEY DON'T WANT TO REUSE A PAINT THEN JUST ASK WHAT THE NEW PAINT SHOULD BE
                            elif useSamePaint == 'n':
                                paint = paintSelection(i+1, isExterior)
                                paintList.append(paint)
                                tempCost = paint.costForArea(wallList[i].area, i+1)
                                print(f"Wall #{i+1} will cost ${tempCost}")
                                cost += tempCost
                            else:
                                print("Please enter a valid answer")
                    else:
                        #if doesnt work just put this back right after the for loop and get rid of if else
                        paint = paintSelection(i+1, isExterior)
                        paintList.append(paint)
                        tempCost = paint.costForArea(wallList[i].area, i+1)
                        print(f"Wall #{i+1} will cost ${tempCost}")
                        cost += tempCost
            else:
                print("Please enter a valid answer")
    else:
        paint = paintSelection(0, isExterior)
        #FIND THE COST
        cost = paint.costForArea(area, 0)

    return cost

#ERROR HANDLING TO MAKE SURE A VALID PAINT TYPE IS CHOSEN
def paintCheck (wallNum):
    if wallNum == 0:
        paintFlag = 0
        while paintFlag == 0:
            paintType = input('\nWhat type of paint would you like to buy\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
            
            if paintType == 'regular' or paintType == 'premium' or paintType == 'diamond':
                paintFlag = 1
            else:
                print("\nPlease enter regular, premium, or diamond\n")
    else:
        paintFlag = 0
        while paintFlag == 0:
            paintType = input(f'\nWhat type of paint would you like to buy for wall {wallNum}\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
            
            if paintType == 'regular' or paintType == 'premium' or paintType == 'diamond':
                paintFlag = 1
            else:
                print("\nPlease enter regular, premium, or diamond\n")
    return paintType

#ERROR HANDLING TO MAKE SURE A VALID SHEEN TYPE IS CHOSEN
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


#GET INFO FOR HOW MANY WALLS,WINDOWS AND DOORS AND THEIR DIMENSIONS
def getWallInfo(numWalls, wallList, insideOrOutside, roomName):
    #IF MORE THAN ONE WALL
    if numWalls > 1:
        sameSize = ''
    #ERROR HANDLING, CHECK IF Y OR N HAS BEEN ENTERED
        while sameSize != 'y' and sameSize != 'n':
            if insideOrOutside == 'inside':
                sameSize = input(f'Are the {roomName} walls the same dimensions?(y/n):\n')
            else:
                sameSize = input(f'Are the {insideOrOutside} walls of the house the same dimensions?(y/n):\n')

            #SAME DIMENSIONS
            if sameSize == 'y':
                width = inputNum('What is the width of the walls in ft?:\n')
                height = inputNum('What is the height of the walls in ft?:\n')
                for i in range(numWalls):
                    wallList.append(Wall(width, height))
                    wallList[i].addWindow(i+1)
                    wallList[i].addDoor(i+1)

            #DIFFERENT DIMENSIONS
            elif sameSize == 'n':
                for i in range(numWalls):
                    width = inputNum(f'What is the width of wall #{i+1} in ft?:\n')
                    height = inputNum(f'What is the height of wall #{i+1} in ft?:\n')
                    wallList.append(Wall(width, height))

                    #SEE IF THERE ARE ANY WINDOWS ON THIS WALL
                    wallList[i].addWindow(i+1)
                    #ANY DOORS ON THE WALL
                    wallList[i].addDoor(i+1)

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
        wallList.append(tempWall)
    
    return wallList

#PRINT AREA INFOR FOR ALL WALLS, WINDOWS AND DOORS
def printAreaInfo(wallList):
    #FIND THE TOTAL AREA
    totalArea = listArea(wallList)
    for i in range(len(wallList)):
        numWindows = len(wallList[i].windowList)
        if numWindows > 0:
            print(f"\nWall #{i+1} contains {numWindows} window(s)")
            for j in range(numWindows):
                print(f"Window #{j+1} is {wallList[i].windowList[j].area} sqft in area")
                
        numDoors = len(wallList[i].doorList)
        if numDoors > 0:
            print(f"\nWall #{i+1} contains {numDoors} door(s)")
            for j in range(numDoors):
                print(f"Door #{j+1} is {wallList[i].doorList[j].area} sqft in area")

                if wallList[i].doorList[j].painted == True:
                    print(f"This door will be painted, therefor it will not subtract from the total area to be painted")

        print(f"Wall #{i+1} Total Area To Paint: {wallList[i].area} sqft\n")

    return totalArea
###########################################################################################################
#OBJECT CLASSES
########################################
#PAINT OBJECT FOR TYPES OF PAINT
class Paint:
    #CONSTRUCTOR CONTAINING TYPE OR QUALITY, SHEEN, COLOR, AND IF IT'S INTERIOR OR EXTERIOR
    def __init__ (self, isExterior, type, sheen, color):
        self.isExterior = isExterior
        self.type = type
        self.sheen = sheen
        self.color = color
        #self.cost = self.findCost()

    #PRINT METHOD TO PRINT THE OBJECTS INFO
    def printPaint (self):
        #print('\nYOUR PAINT INFO:')
        print(f"Color: {self.color}")
        print(f"Quality: {self.type}")
        print(f"Finish: {self.sheen}")
        if self.isExterior == 'y':
            print("In/Ex: exterior\n")
        elif self.isExterior == 'n':
            print("In/Ex: interior\n")

    #FINDS THE COST OF THE OBJECT PER GALLON
    #could probably just put this into costForArea function
    def findCost (self):
        cost = 0
        if self.isExterior == 'y':
            cost = 10
        paintType = {'regular': 10, 'premium': 20, 'diamond': 30}
        sheen = {'semi_gloss': 6, 'satin': 4, 'flat': 2}
        cost += paintType.get(self.type) + sheen.get(self.sheen)
        return cost
    
    #FINDS THE COST OF THE PAINT FOR A GIVEN AREA
    def costForArea (self, area, wallNum):
        paintCost = self.findCost()

        #NUMBER OF GALLONS NEEDED TO COVER THE AREA
        numGallons = area/400
        numPrimer = 0

        if wallNum == 0:
            #ACCOUNTING FOR COATS (DIAMOND ONLY NEEDS 1)
            match self.type:
                case 'regular':
                    print(f"Your paint costs ${paintCost} per gallon + $10 per gallon of Primer")
                    #IF REGULAR NEEDs PRIMER
                    numPrimer = ceil(numGallons)
                    #2 COATS FOR REGULAR
                    numGallons = ceil(numGallons*2)
                    print(f"You will need {numGallons} gallon(s) of paint")
                    print(f"You will need {numPrimer} gallon(s) of primer")
                
                case 'premium':
                    print(f"Your paint costs ${paintCost} per gallon")
                    #2 COATS FOR PRIMER
                    numGallons = ceil(numGallons*2)
                    print(f"You will need {numGallons} gallon(s) of paint")
                case _:
                    print(f"Your paint costs ${paintCost} per gallon")
                    numGallons = ceil(numGallons)
                    print(f"You will need {numGallons} gallon(s) of paint")
        else:
            match self.type:
                case 'regular':
                    print(f"Your paint costs ${paintCost} per gallon + $10 per gallon of Primer for wall #{wallNum}")
                    #IF REGULAR NEEDs PRIMER
                    numPrimer = ceil(numGallons)
                    #2 COATS FOR REGULAR
                    numGallons = ceil(numGallons*2)
                    print(f"You will need {numGallons} gallon(s) of paint for wall #{wallNum}")
                    print(f"You will need {numPrimer} gallon(s) of primer for wall #{wallNum}")
                case 'premium':
                    print(f"Your paint costs ${paintCost} per gallon for wall #{wallNum}")
                    #2 COATS FOR PRIMER
                    numGallons = ceil(numGallons*2)
                    print(f"You will need {numGallons} gallon(s) of paint for wall #{wallNum}")
                case _:
                    print(f"Your paint costs ${paintCost} per gallon for wall #{wallNum}")
                    numGallons = ceil(numGallons)
                    print(f"You will need {numGallons} gallon(s) of paint for wall #{wallNum}")
        #EXTERIOR COST CALCULATION AND PRINT
        cost = (numGallons * paintCost) + (numPrimer * 10)
        return cost

########################################
#WALL OBJECT
class Wall:
    #CONSTRUCTOR WITH WIDTH AND HEIGHT AND AN EMPTY LIST OF WINDOWS AND DOORS, AUTOMATICALLY CREATES AREA
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = area(width, height)
        self.windowList = []
        self.doorList = []

    #ADD WINDOW METHOD FOR WALLS, ASKS FOR THE WIDTH AND HEIGHT OF THE WINDOW AND ADDS IT TO THE WALLS WINDOW LIST
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

    #ADD DOOR METHOD FOR WALLS, ASKS FOR THE WIDTH AND HEIGHT AND IF THE DOOR SHOULD BE PAINTED TOO AND ADDS IT TO THE WALLS DOOR LIST
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
                    else:
                        print('Please enter a valid answer')

                    self.doorList.append(newDoor)

            else:
                return
########################################
#WINDOW OR DOOR OBJECT, DOESN'T NEED TO BE DIFFERENT BECAUSE PRETTY MUCH ONLY USING AREA, DOORS NEED THE PAINTED ATTRIBUTE
#WINDOWS PAINTED ATTRIBUTE IT AUTOMATICALLY SET TO FALSE, AND USER IS NOT GIVEN A CHANCE TO CHANGE THAT
class WindowOrDoor:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = area(width, height)
        self.painted = False
########################################
class Room:
    def __init__ (self, name, wallList, paintArea):
        self.name = name
        self.wallList = wallList
        self.paintArea = paintArea
########################################
#PAINT JOB OBJECT, TO KEEP TRACK OF OUTSIDE AND INSIDE PAINT JOBS, CONTAINS A COST AND AN AREA
class PaintJob:
    def __init__(self, cost, area, insideOrOutside):
        self.cost = cost
        self.area = area
        self.inOrOut = insideOrOutside

#TTRYING WITH ROOMS
    def calcPaintJob(self):
        #FOR OUTSIDE PAINT JOB
        if self.inOrOut == 'outside':
            #WALL INFO
            numWalls = inputNum(f'How many walls on the outside of the house are you painting?:\n')
            wallList = []
            
            wallList = getWallInfo(numWalls, wallList, 'outside', '')

            #PRINT AREA INFO
            area = printAreaInfo(wallList)
            print(f"Total outside area to be painted: {area} sqft\n")
            self.area += area

            #CHOOSE PAINT
            cost = choosePaint(area, wallList, numWalls, 'y')
            print(f"\nYour entire {self.inOrOut} paint job will cost ${cost}\n")
            self.cost += cost

        #FOR INSIDE PAINT JOB
        elif self.inOrOut == 'inside':
            numRooms = inputNum(f'How many rooms on the inside of the house are you painting?:\n')
            roomList = []
            insideCost = 0
            insideArea = 0
            for i in range(numRooms):
                wallList = []
                roomName = input(f"What is the name of room #{i + 1}?:\n")
                numWalls = inputNum(f'How many walls in the {roomName} are you painting?:\n')
                wallList = getWallInfo(numWalls, wallList, 'inside', roomName)
                area = printAreaInfo(wallList)
                roomList.append(Room(roomName, wallList, area))
                print(f"Total area to be painted in the {roomName}: {area} sqft\n")
                insideArea += area

                #CHOOSE PAINT FOR THE ROOM
                cost = choosePaint(area, wallList, numWalls, 'n')
                print(f"\nYour {roomName} paint job will cost ${cost}\n")
                insideCost += cost
            self.cost += insideCost
            self.area += insideArea
            print(f"Total inside area to be painted: {insideArea} sqft")
            print(f"\nYour entire inside paint job will cost ${insideCost}\n")
            
##############################################################################################################
#MAIN
if __name__ == '__main__':
    print("\nWELCOME TO THE HOUSE PAINTER CALCULATOR!\n########################################################\n")
    #WHILE STATEMENT TO LOOP UNTIL A VALID ANSWER HAS BEEN GIVEN
    mainLoopFlag = False
    while mainLoopFlag != True:
        outsideOrInside = input('Are you planning on painting the outside (o), the inside (i), or both (b)?:\n')
        match outsideOrInside:
    #############################################################################
            #OUTSIDE
            case 'o':
                #CREATE NEW PAINT JOB OBJECT
                outPaintJob = PaintJob(0, 0, 'outside')
                #FIGURE OUT THE COST AND AREA
                outPaintJob.calcPaintJob()
                mainLoopFlag = True
    #############################################################################
            #INSIDE
            case 'i':
                #CREATE NEW PAINT JOB
                inPaintJob = PaintJob(0, 0, 'inside')
                #FIGURE OUT THE COST AND AREA
                inPaintJob.calcPaintJob()
                mainLoopFlag = True

    #############################################################################
            #BOTH
            case 'b':
                totalArea = 0
                totalCost = 0

                #MAKE AND FILL OUT OUTSIDE PAINT JOB
                outPaintJob = PaintJob(0, 0, 'outside')
                outPaintJob.calcPaintJob()

                #ADD TO TOTALS
                totalArea = outPaintJob.area
                totalCost = outPaintJob.cost

                #CREATE AND FILL OUT INSIDE PAINT JOB
                inPaintJob = PaintJob(0, 0, 'inside')
                inPaintJob.calcPaintJob()

                #ADD TO TOTALS
                totalArea += inPaintJob.area
                totalCost += inPaintJob.cost
                
                print(f"\nYour total paint job will cover {totalArea} sqft and cost ${totalCost}\n")
                mainLoopFlag = True
    #############################################################################
            #INVALID ANSWER
            case _:
                print("Please enter a valid answer")
