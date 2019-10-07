import pygame
class Obsticales:
    def __init__(self,surface, color):
        self.surface = surface
        self.theme = color
        self.rectObj = pygame.rect.Rect(1000, 500, 20, 50)
        self.wait = 0
    def move(self):
        if not self.wait == 3:
            self.rectObj.move_ip(-5, 0)
            self.wait = 0
        else:
            self.wait += 1
    def BorderCheck(self):
        if self.rectObj[0] < -20:
            self.rectObj[0] = 1000
    def update(self):
        self.move()
        self.BorderCheck()
        pygame.draw.rect(self.surface, self.theme, self.rectObj)
