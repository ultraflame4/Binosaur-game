import GameEngine.Obsticales.groundObj as groundObj
class groundObstacles:
    def __init__(self, surface, color):
        self.surface = surface
        self.color = color
        self.createObj()
    def createObj(self):
        self.groundObstacle0 = groundObj.Obsticales(self.surface, self.color)
        self.groundObstacle1 = groundObj.Obsticales(self.surface, self.color, 1050)
        self.groundObstacle2 = groundObj.Obsticales(self.surface, self.color, 1300)
        self.groundObstacle3 = groundObj.Obsticales(self.surface, self.color, 1500)

    def draw(self):
        self.groundObstacle0.update()
        self.groundObstacle1.update()
        self.groundObstacle2.update()
        self.groundObstacle3.update()
