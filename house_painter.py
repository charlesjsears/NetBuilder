#THESE ARE NEW CHANGES MADE FROM GITHUB
#These Are some new changes for branch number 2
#changing again for a pull request

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
