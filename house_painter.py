#THESE ARE NEW CHANGES MADE FROM GITHUB
#These Are some new changes for branch number 2
#changing again for a pull request
def area(width, height):
    return width * height

def listArea(wallList):
    total = 0
    for i in range(len(wallList)):
        total += wallList[i].area
    return total

class Paint:
    def __init__ (self, isExterior, type, sheen, color):
        self.isExterior = isExterior
        self.type = type
        self.sheen = sheen
        self.color = color
        self.cost = self.findCost()

    def findCost (self):
        cost = 0
        if self.isExterior == 1:
            cost = 10
        paintType = {'regular': 10, 'premium': 20, 'diamond': 30}
        sheen = {'semi_gloss': 6, 'satin': 4, 'flat': 2}
        cost += paintType.get(self.type) + sheen.get(self.sheen)
        if self.type == 'regular':
            cost = (cost*2) + 10
        elif self.type == 'premium':
            cost *= 2
        return cost

class Wall:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = area(width, height)

print("Welcome to the house paint calculator!")
totalArea = 0
totalCost = 0
outsideOrInside = ''
#PAINT TYPE, PREMIUM NEEDS 2 COATS, REGULAR NEEDS 2 WITH PRIMER, DIAMOND NEEDS 1 COAT
#add 10 for exterior paint
#paintType = {'regular': 10, 'premium': 20, 'diamond': 30, 'primer': 10}
#sheen = {'semi_gloss': 6, 'satin': 4, 'flat': 2}

while (outsideOrInside != 'o') and (outsideOrInside != 'b') and (outsideOrInside != 'i'):
    outsideOrInside = input('Are you planning on painting the outside (o), the inside (i), or both (b)?:')

    #OUTSIDE
    if outsideOrInside == 'o' or outsideOrInside == 'b':
        numOutWalls = int(input('How many walls on the outside of the house are you painting?:'))
        outWalls = []
        sameSize = ''
        while sameSize != 'y' and sameSize != 'n':
            sameSize = input('Are the outside walls of the house the same dimensions?(y/n):')

            #DIFFERENT DIMENSIONS
            if sameSize == 'n':
                for i in range(numOutWalls):
                    width = int(input(f'What is the width of wall #{i} in ft?:'))
                    height = int(input(f'What is the height of wall #{i} in ft?:'))
                    outWalls.append(Wall(width, height))

            #SAME DIMENSIONS
            elif sameSize == 'y':
                width = int(input(f'What is the width of the walls in ft?:'))
                height = int(input(f'What is the height of the walls in ft?:'))
                for i in range(numOutWalls):
                    outWalls.append(Wall(width, height))
            #INVALID RESPONSE
            else:
                print("Please enter a valid answer")
        
        exArea = listArea(outWalls)
        totalArea += exArea

        #PAINT TYPES
        samePaint = ''
        while samePaint != 'y' and samePaint != 'n':
            samePaint = input('Do you want all the walls to have the same paint?(y/n):')
            #SAME PAINT
            if samePaint == 'y':
                paintType = input('What type of paint would you like to buy\nRegular Paint (type regular) - $10 - 2 Coats + 1 Primer Coat - Primer - $10\nPremium Paint (type premium) - $20 - 2 Coats\nDiamond Paint (type diamond) - $30 - 1 Coat:')
                sheenType = input('What type of sheen would you like?\nSemi-Gloss (type semi_gloss) - $6\nSatin (type satin) - $4\nFlat (type flat) - $2:')
                color = input('What color?:')
                exPaint = Paint('y', paintType, sheenType, color)
                paintCost = exPaint.cost
                print(f"You're using {exPaint.type} exterior {exPaint.sheen} {exPaint.color} paint")
                exCost = (exArea / 400) * paintCost
                print(f"Your exterior paint job will cost {totalCost}")
                totalCost += exCost
    #INSIDE
    elif outsideOrInside == 'i' or outsideOrInside == 'b':
        numInWalls = int(input('How many walls on the inside of the house are you painting?:'))
        sameSize = input('Are the walls the same dimensions?(y/n):')
        inWalls = []
        while sameSize != 'y' or sameSize != 'n':
            if sameSize == 'n':
                for i in range(numInWalls):
                    width = int(input(f'What is the width of wall #{i} in ft?:'))
                    height = int(input(f'What is the height of wall #{i} in ft?:'))
                    inWalls[i] = Wall(width, height)
            elif sameSize == 'y':
                width = int(input(f'What is the width of the walls in ft?:'))
                height = int(input(f'What is the height of the walls in ft?:'))
                for i in range(numInWalls):
                    inWalls[i] = Wall(width, height)
            else:
                print("Please enter a valid answer")
        totalArea += listArea(inWalls)
    else:
        print("Please enter a valid answer")

sqftPerGallons = 400
costPerGallon = 20
numGallons = totalArea/sqftPerGallons
cost = numGallons * costPerGallon
print(f'It will take {numGallons} gallons of paint and will cost {cost} dollars')

"""
roomOrWall = input('Are you planning on painting more than one wall?(y/n):')
totalArea = 0
if roomOrWall == 'n':
    wallWidth = int(input('What is the width of the wall?:'))
    wallHeight = int(input('What is the height of the wall?:'))
    wallArea = area(wallWidth, wallHeight)
    totalArea += wallArea
elif roomOrWall == 'y':
    numWalls = int(input('How many walls do you want to paint'))
numRooms = int(input('how many rooms are you planning to paint?:'))


numWallsPerRoom = []
i = 0
for i in range(numRooms):
    numWallsPerRoom[i] = i
    #numWallsPerRoom[i] = int(input('how many walls are you painting:'))


paintPerWall = input('how much paint do you need to paint a wall?:')

totalPaint = 0
for i in numRooms:
    totalPaint += numWallsPerRoom[i]*paintPerWall

print("total gallons of paint needed: ", totalPaint)

totalCost = totalPaint * 25

print("total cost:", totalCost)

#maybe different colors
#dont want to paint windows or doors
#don't paint sockets
#different sized windows
#types of paint, different costs
#create a calculaator for how much money it will cost
#use everything we have covered
#find total paint in gallons and price
#ask for length and hieght of each room
#find the most cost effective method

"""