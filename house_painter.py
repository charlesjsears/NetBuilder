
#FUNCTIONS
def area(width, height):
    return width * height

def listArea(wallList):
    total = 0
    for i in range(len(wallList)):
        total += wallList[i].area
        #print(total)
    return total

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

    def findCost (self):
        cost = 0
        if self.isExterior == 'y':
            cost = 10
        paintType = {'regular': 10, 'premium': 20, 'diamond': 30}
        sheen = {'semi_gloss': 6, 'satin': 4, 'flat': 2}
        cost += paintType.get(self.type) + sheen.get(self.sheen)
        return cost

class Wall:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = area(width, height)

print("Welcome to the house paint calculator!\n")
totalArea = 0
totalCost = 0
outsideOrInside = ''
exArea = 0
#PAINT TYPE, PREMIUM NEEDS 2 COATS, REGULAR NEEDS 2 WITH PRIMER, DIAMOND NEEDS 1 COAT
#add 10 for exterior paint

while (outsideOrInside != 'o') and (outsideOrInside != 'i'):
    outsideOrInside = input('Are you planning on painting the outside (o) or the inside (i)?:\n')

    #OUTSIDE
    if outsideOrInside == 'o':
        numOutWalls = int(input('How many walls on the outside of the house are you painting?:\n'))
        outWalls = []
        sameSize = ''
        while sameSize != 'y' and sameSize != 'n':
            sameSize = input('Are the outside walls of the house the same dimensions?(y/n):\n')

            #DIFFERENT DIMENSIONS
            if sameSize == 'n':
                for i in range(numOutWalls):
                    width = int(input(f'What is the width of wall #{i+1} in ft?:\n'))
                    height = int(input(f'What is the height of wall #{i+1} in ft?:\n'))
                    outWalls.append(Wall(width, height))

            #SAME DIMENSIONS
            elif sameSize == 'y':
                width = int(input(f'What is the width of the walls in ft?:\n'))
                height = int(input(f'What is the height of the walls in ft?:\n'))
                for i in range(numOutWalls):
                    outWalls.append(Wall(width, height))

            #INVALID RESPONSE
            else:
                print("Please enter a valid answer\n")
        
        exArea = listArea(outWalls)
        print(f"Exterior Area to be painted: {exArea}\n")
        #totalArea += exArea

        #PAINT TYPES
        samePaint = ''
        while samePaint != 'y' and samePaint != 'n':
            samePaint = input('Do you want all the walls to have the same paint?(y/n):\n')
            #SAME PAINT
            if samePaint == 'y':
                #COLLECT PAINT INFO
                paintType = input('What type of paint would you like to buy\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
                sheenType = input('What type of sheen would you like?\nSemi-Gloss (type semi_gloss) - $6\nSatin (type satin) - $4\nFlat (type flat) - $2:\n')
                color = input('What color?:\n')

                #CREATE PAINT OBJECT & PRINT INFO
                exPaint = Paint('y', paintType, sheenType, color)
                exPaint.printPaint()

                #FIND & PRINT COST PER GALLON
                paintCost = exPaint.findCost()
                print(f"Your paint costs ${paintCost} per gallon")

                #NUMBER OF GALLONS NEEDED TO COVER THE AREA
                numGallons = (exArea/400)
                numPrimer = 0
                #ACCOUNTING FOR COATS (DIAMOND ONLY NEEDS 1)
                if exPaint.type == 'regular':
                    #IF REGULAR NEED PRIMER
                    numPrimer = numGallons
                    #2 COATS FOR REGULAR
                    numGallons *= 2
                    print(f"You will need {numGallons} gallons of paint")
                    print(f"You will need {numPrimer} gallons of primer")
                elif exPaint.type == 'premium':
                    #2 COATS FOR PRIMER
                    numGallons *= 2
                    print(f"You will need {numGallons} gallons of paint")

                #EXTERIOR COST CALCULATION AND PRINT
                exCost = (numGallons * paintCost) + (numPrimer * 10)
                print(f"Your exterior paint job will cost ${exCost}\n")
                #totalCost += exCost

            #DIFFERENT PAINT
            elif samePaint == 'n':
                exCost = 0
                for i in range(len(outWalls)):
                    print(f"PAINT INFO FOR WALL #{i+1}")
                    paintType = input(f'What type of paint would you like to buy for wall {i+1}\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
                    sheenType = input(f'What type of sheen or finish would you like for wall {i+1}?\nSemi-Gloss (type semi_gloss) - $6\nSatin (type satin) - $4\nFlat (type flat) - $2:\n')
                    color = input(f'What color for wall {i+1}?:\n')

                    #CREATE PAINT OBJECT & PRINT INFO
                    exPaint = Paint('y', paintType, sheenType, color)
                    exPaint.printPaint()

                    #FIND & PRINT COST PER GALLON
                    paintCost = exPaint.findCost()
                    print(f"Your paint for wall {i+1} costs ${paintCost} per gallon")

                    #NUMBER OF GALLONS NEEDED TO COVER THE AREA
                    numGallons = (outWalls[i].area/400)
                    numPrimer = 0

                    #ACCOUNTING FOR COATS (DIAMOND ONLY NEEDS 1)
                    if exPaint.type == 'regular':
                        #IF REGULAR NEED PRIMER
                        numPrimer = numGallons
                        #2 COATS FOR REGULAR
                        numGallons *= 2
                        print(f"You will need {numPrimer} gallons of primer for wall {i+1}")
                    elif exPaint.type == 'premium':
                        #2 COATS FOR PRIMER
                        numGallons *= 2

                    print(f"You will need {numGallons} gallons of paint for wall {i+1}")
                    #EXTERIOR COST CALCULATION AND PRINT
                    tempCost = (numGallons * paintCost) + (numPrimer * 10)
                    exCost += tempCost
                    print(f"Wall {i+1} will cost ${tempCost} to paint\n")

                print(f"Your exterior paint job will cost ${exCost}\n")
                #totalCost += exCost
            else:
                print("Please enter a valid answer")

    #INSIDE
    elif outsideOrInside == 'i':
        numInWalls = int(input('How many walls on the inside of the house are you painting?:\n'))
        inWalls = []
        sameSize = ''
        while sameSize != 'y' and sameSize != 'n':
            sameSize = input('Are the inside walls of the house the same dimensions?(y/n):\n')

            #DIFFERENT DIMENSIONS
            if sameSize == 'n':
                for i in range(numInWalls):
                    width = int(input(f'What is the width of wall #{i+1} in ft?:\n'))
                    height = int(input(f'What is the height of wall #{i+1} in ft?:\n'))
                    inWalls.append(Wall(width, height))

            #SAME DIMENSIONS
            elif sameSize == 'y':
                width = int(input(f'What is the width of the walls in ft?:\n'))
                height = int(input(f'What is the height of the walls in ft?:\n'))
                for i in range(numInWalls):
                    inWalls.append(Wall(width, height))

            #INVALID RESPONSE
            else:
                print("Please enter a valid answer\n")
        
        inArea = listArea(inWalls)
        print(f"Interior Area to be painted: {inArea}\n")
        totalArea += inArea

        #PAINT TYPES
        samePaint = ''
        while samePaint != 'y' and samePaint != 'n':
            samePaint = input('Do you want all the walls to have the same paint?(y/n):\n')
            #SAME PAINT
            if samePaint == 'y':
                #COLLECT PAINT INFO
                paintType = input('What type of paint would you like to buy\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
                sheenType = input('What type of sheen would you like?\nSemi-Gloss (type semi_gloss) - $6\nSatin (type satin) - $4\nFlat (type flat) - $2:\n')
                color = input('What color?:\n')

                #CREATE PAINT OBJECT & PRINT INFO
                inPaint = Paint('n', paintType, sheenType, color)
                inPaint.printPaint()

                #FIND & PRINT COST PER GALLON
                paintCost = inPaint.findCost()
                print(f"Your paint costs ${paintCost} per gallon")

                #NUMBER OF GALLONS NEEDED TO COVER THE AREA
                numGallons = (inArea/400)
                numPrimer = 0
                #ACCOUNTING FOR COATS (DIAMOND ONLY NEEDS 1)
                if inPaint.type == 'regular':
                    #IF REGULAR NEED PRIMER
                    numPrimer = numGallons
                    #2 COATS FOR REGULAR
                    numGallons *= 2
                    print(f"You will need {numGallons} gallons of paint")
                    print(f"You will need {numPrimer} gallons of primer")
                elif inPaint.type == 'premium':
                    #2 COATS FOR PRIMER
                    numGallons *= 2
                    print(f"You will need {numGallons} gallons of paint")

                #INTERIOR COST CALCULATION AND PRINT
                inCost = (numGallons * paintCost) + (numPrimer * 10)
                print(f"Your interior paint job will cost ${inCost}\n")
                totalCost += inCost

            #DIFFERENT PAINT
            elif samePaint == 'n':
                inCost = 0
                for i in range(len(inWalls)):
                    print(f"PAINT INFO FOR WALL #{i+1}")
                    paintType = input(f'What type of paint would you like to buy for wall {i+1}\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat for $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat\n:')
                    sheenType = input(f'What type of sheen or finish would you like for wall {i+1}?\nSemi-Gloss (type semi_gloss) - $6\nSatin (type satin) - $4\nFlat (type flat) - $2:\n')
                    color = input(f'What color for wall {i+1}?:\n')

                    #CREATE PAINT OBJECT & PRINT INFO
                    inPaint = Paint('y', paintType, sheenType, color)
                    inPaint.printPaint()

                    #FIND & PRINT COST PER GALLON
                    paintCost = inPaint.findCost()
                    print(f"Your paint for wall {i+1} costs ${paintCost} per gallon")

                    #NUMBER OF GALLONS NEEDED TO COVER THE AREA
                    numGallons = (inWalls[i].area/400)
                    numPrimer = 0

                    #ACCOUNTING FOR COATS (DIAMOND ONLY NEEDS 1)
                    if inPaint.type == 'regular':
                        #IF REGULAR NEED PRIMER
                        numPrimer = numGallons
                        #2 COATS FOR REGULAR
                        numGallons *= 2
                        print(f"You will need {numPrimer} gallons of primer for wall {i+1}")
                    elif inPaint.type == 'premium':
                        #2 COATS FOR PRIMER
                        numGallons *= 2

                    print(f"You will need {numGallons} gallons of paint for wall {i+1}")
                    #EXTERIOR COST CALCULATION AND PRINT
                    tempCost = (numGallons * paintCost) + (numPrimer * 10)
                    inCost += tempCost
                    print(f"Wall {i+1} will cost ${tempCost} to paint\n")

                print(f"Your exterior paint job will cost ${inCost}\n")
                totalCost += inCost
    else:
        print("Please enter a valid answer")

"""
#dont want to paint windows or doors
#don't paint sockets
#different sized windows
#find total paint in gallons and price
#find the most cost effective method

"""