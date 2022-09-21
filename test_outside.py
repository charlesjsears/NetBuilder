#ERROR HANDLING TO MAKE SURE A VALID PAINT TYPE IS CHOSEN
class Wall:
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.area = width*height

def listArea(wallList):
    total = 0
    for i in range(len(wallList)):
        total += wallList[i].area
        #print(total)
    return total

class TestClassDemoInstance:
    value = 0

    def test_answer(self):
        wall1 = Wall(5, 20)
        wall2 = Wall(4, 25)
        wall3 = Wall(10, 10)
        list = [wall1, wall2, wall3]
        assert listArea(list) == 300
        #assert listArea(list) == 301
