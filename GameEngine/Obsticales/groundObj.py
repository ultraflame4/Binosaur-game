import pygame
import random
class Obsticales:
    def __init__(self,surface, color, playerRect ,dist=1000):
        self.surface = surface
        self.theme = color
        self.rectObj = pygame.rect.Rect(dist, 500, 20, 50)
        self.playerRect = playerRect
        self.detector = pygame.rect.Rect((self.rectObj[0] + 5), 0, 10, 500)
        self.speed = 5
        self.maxSpeed = 20
    def jumpOver(self):
        if self.detector.colliderect(self.playerRect):
            return True
    def move(self):
        if self.speed < 1:
            self.speed = 1
        elif self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        self.rectObj.move_ip((-1 * self.speed), 0)
        self.detector = pygame.rect.Rect((self.rectObj[0] + 5), 0, 10, 500)

    def BorderCheck(self):
        if self.rectObj[0] < -20:
            self.rectObj[0] = (1000 + (random.randint(1, 50) * 10))

    def update(self):
        self.move()
        self.BorderCheck()
        pygame.draw.rect(self.surface, self.theme, self.rectObj)
